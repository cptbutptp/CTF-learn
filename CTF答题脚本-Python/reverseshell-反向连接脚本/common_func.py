#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function, unicode_literals, division, absolute_import
import sys
import time
import binascii
import struct
import collections
import logging
import socket
import select
import threading
import traceback
import functools

try:
    # for pycharm type hinting
    from typing import Union, Callable
except:
    pass

# socket recv buffer, 16384 bytes
RECV_BUFFER_SIZE = 2 ** 14

# default secretkey, use -k/--secretkey to change
SECRET_KEY = "shootback"

# how long a SPARE slaver would keep
# once slaver received an heart-beat package from master,
#   the TTL would be reset. And heart-beat delay is less than TTL,
#   so, theoretically, spare slaver never timeout,
#   except network failure
# notice: working slaver would NEVER timeout
SPARE_SLAVER_TTL = 300

# internal program version, appears in CtrlPkg
INTERNAL_VERSION = 0x000D

# version for human readable
__version__ = (2, 2, 8, INTERNAL_VERSION)

# just a logger
log = logging.getLogger(__name__)


def version_info():
    """get program version for human. eg: "2.1.0-r2" """
    return "{}.{}.{}-r{}".format(*__version__)


def configure_logging(level):
    logging.basicConfig(
        level=level,
        format='[%(levelname)s %(asctime)s] %(message)s',
    )


def fmt_addr(socket):
    """(host, int(port)) --> "host:port" """
    return "{}:{}".format(*socket)


def split_host(x):
    """ "host:port" --> (host, int(port))"""
    try:
        host, port = x.split(":")
        port = int(port)
    except:
        raise ValueError(
            "wrong syntax, format host:port is "
            "required, not {}".format(x))
    else:
        return host, port


def try_close(closable):
    """try close something

    same as
        try:
            connection.close()
        except:
            pass
    """
    try:
        closable.close()
    except:
        pass


def select_recv(conn, buff_size, timeout=None):
    """add timeout for socket.recv()
    :type conn: socket.SocketType
    :type buff_size: int
    :type timeout: float
    :rtype: Union[bytes, None]
    """
    rlist, _, _ = select.select([conn], [], [], timeout)
    if not rlist:
        # timeout
        raise RuntimeError("recv timeout")

    buff = conn.recv(buff_size)
    if not buff:
        raise RuntimeError("received zero bytes, socket was closed")

    return buff


class SocketBridge:
    """
    transfer data between sockets
    """

    def __init__(self):
        self.conn_rd = set()  # record readable-sockets
        self.map = {}  # record sockets pairs
        self.callbacks = {}  # record callbacks

    def add_conn_pair(self, conn1, conn2, callback=None):
        """
        transfer anything between two sockets

        :type conn1: socket.SocketType
        :type conn2: socket.SocketType
        :param callback: callback in connection finish
        :type callback: Callable
        """
        # mark as readable
        self.conn_rd.add(conn1)
        self.conn_rd.add(conn2)

        # record sockets pairs
        self.map[conn1] = conn2
        self.map[conn2] = conn1

        # record callback
        if callback is not None:
            self.callbacks[conn1] = callback

    def start_as_daemon(self):
        t = threading.Thread(target=self.start)
        t.daemon = True
        t.start()
        log.info("SocketBridge daemon started")
        return t

    def start(self):
        while True:
            try:
                self._start()
            except:
                log.error("FATAL ERROR! SocketBridge failed {}".format(
                    traceback.format_exc()
                ))

    def _start(self):
        # memoryview act as an recv buffer
        # refer https://docs.python.org/3/library/stdtypes.html#memoryview
        buff = memoryview(bytearray(RECV_BUFFER_SIZE))
        while True:
            if not self.conn_rd:
                # sleep if there is no connections
                time.sleep(0.06)
                continue

            # blocks until there is socket(s) ready for .recv
            # notice: sockets which were closed by remote,
            #   are also regarded as read-ready by select()
            r, w, e = select.select(self.conn_rd, [], [], 0.5)

            for s in r:  # iter every read-ready or closed sockets
                try:
                    # here, we use .recv_into() instead of .recv()
                    #   recv data directly into the pre-allocated buffer
                    #   to avoid many unnecessary malloc()
                    # see https://docs.python.org/3/library/socket.html#socket.socket.recv_into
                    rec_len = s.recv_into(buff, RECV_BUFFER_SIZE)
                except:
                    # unable to read, in most cases, it's due to socket close
                    self._rd_shutdown(s)
                    continue

                if not rec_len:
                    # read zero size, closed or shutdowned socket
                    self._rd_shutdown(s)
                    continue

                try:
                    # send data, we use `buff[:rec_len]` slice because
                    #   only the front of buff is filled
                    self.map[s].send(buff[:rec_len])
                except:
                    # unable to send, close connection
                    self._rd_shutdown(s)
                    continue

    def _rd_shutdown(self, conn, once=False):
        """action when connection should be read-shutdown
        :type conn: socket.SocketType
        """
        if conn in self.conn_rd:
            self.conn_rd.remove(conn)

        try:
            conn.shutdown(socket.SHUT_RD)
        except:
            pass

        if not once and conn in self.map:  # use the `once` param to avoid infinite loop
            # if a socket is rd_shutdowned, then it's
            #   pair should be wr_shutdown.
            self._wr_shutdown(self.map[conn], True)

        if self.map.get(conn) not in self.conn_rd:
            # if both two connection pair was rd-shutdowned,
            #   this pair sockets are regarded to be completed
            #   so we gonna close them
            self._terminate(conn)

    def _wr_shutdown(self, conn, once=False):
        """action when connection should be write-shutdown
        :type conn: socket.SocketType
        """
        try:
            conn.shutdown(socket.SHUT_WR)
        except:
            pass

        if not once and conn in self.map:  # use the `once` param to avoid infinite loop
            #   pair should be rd_shutdown.
            # if a socket is wr_shutdowned, then it's
            self._rd_shutdown(self.map[conn], True)

    def _terminate(self, conn):
        """terminate a sockets pair (two socket)
        :type conn: socket.SocketType
        :param conn: any one of the sockets pair
        """
        try_close(conn)  # close the first socket

        # ------ close and clean the mapped socket, if exist ------
        if conn in self.map:
            _mapped_conn = self.map[conn]
            try_close(_mapped_conn)
            if _mapped_conn in self.map:
                del self.map[_mapped_conn]

            del self.map[conn]  # clean the first socket
        else:
            _mapped_conn = None  # just a fallback

        # ------ callback --------
        # because we are not sure which socket are assigned to callback,
        #   so we should try both
        if conn in self.callbacks:
            try:
                self.callbacks[conn]()
            except Exception as e:
                log.error("traceback error: {}".format(e))
                log.debug(traceback.format_exc())
            del self.callbacks[conn]
        elif _mapped_conn and _mapped_conn in self.callbacks:
            try:
                self.callbacks[_mapped_conn]()
            except Exception as e:
                log.error("traceback error: {}".format(e))
                log.debug(traceback.format_exc())
            del self.callbacks[_mapped_conn]


class CtrlPkg:
    """
    Control Packages of shootback, not completed yet
    current we have: handshake and heartbeat

    NOTICE: If you are non-Chinese reader,
        please contact me for the following Chinese comment's translation
        http://github.com/aploium

    ??????????????? ??????64bytes      CtrlPkg.FORMAT_PKG
    ?????? big-endian

    ??????   ??????        ????????????           ??????
    1    pkg_ver    unsigned char       ?????????  *1
    1    pkg_type    signed char        ????????? *2
    2    prgm_ver    unsigned short    ???????????? *3
    20    N/A          N/A              ??????
    40    data        bytes           ????????? *4

    *1: ?????????. ??????????????????????????????, ???????????? 0x01

    *2: ?????????. ????????????, ????????????????????????Slaver??????, ????????????Master??????
        -1: Slaver-->Master ??????????????????       PTYPE_HS_S2M
         0: ?????????                            PTYPE_HEART_BEAT
        +1: Master-->Slaver ????????????          PTYPE_HS_M2S

    *3: ???????????? INTERNAL_VERSION

    *4: ??????????????????????????????????????????????????????

    -------------- ??????????????? ------------------
    ?????????: -1 (Slaver-->Master ??????????????????)
        ??????   ??????           ????????????         ??????
         4    crc32_s2m   unsigned int     ??????????????? CRC32(Reversed(SECRET_KEY))
       ????????????
       *??????: -1??????????????? SECRET_KEY ?????????????????????CRC32, +1????????????????????????

    ?????????: 0 (??????)
       ???????????????

    ?????????: +1 (Master-->Slaver ????????????)
        ??????   ??????           ????????????         ??????
         4    crc32_m2s   unsigned int     ??????????????? CRC32(SECRET_KEY)
       ????????????

    """
    PACKAGE_SIZE = 2 ** 6  # 64 bytes
    CTRL_PKG_TIMEOUT = 5  # CtrlPkg recv timeout, in second

    # CRC32 for SECRET_KEY and Reversed(SECRET_KEY)
    SECRET_KEY_CRC32 = binascii.crc32(SECRET_KEY.encode('utf-8')) & 0xffffffff
    SECRET_KEY_REVERSED_CRC32 = binascii.crc32(SECRET_KEY[::-1].encode('utf-8')) & 0xffffffff

    # Package Type
    PTYPE_HS_S2M = -1  # handshake pkg, slaver to master
    PTYPE_HEART_BEAT = 0  # heart beat pkg
    PTYPE_HS_M2S = +1  # handshake pkg, Master to Slaver

    TYPE_NAME_MAP = {
        PTYPE_HS_S2M: "PTYPE_HS_S2M",
        PTYPE_HEART_BEAT: "PTYPE_HEART_BEAT",
        PTYPE_HS_M2S: "PTYPE_HS_M2S",
    }

    # formats
    # see https://docs.python.org/3/library/struct.html#format-characters
    #   for format syntax
    FORMAT_PKG = "!b b H 20x 40s"
    FORMATS_DATA = {
        PTYPE_HS_S2M: "!I 36x",
        PTYPE_HEART_BEAT: "!40x",
        PTYPE_HS_M2S: "!I 36x",
    }

    _cache_prebuilt_pkg = {}  # cache

    def __init__(self, pkg_ver=0x01, pkg_type=0,
                 prgm_ver=INTERNAL_VERSION, data=(),
                 raw=None,
                 ):
        """do not call this directly, use `CtrlPkg.pbuild_*` instead"""
        self.pkg_ver = pkg_ver
        self.pkg_type = pkg_type
        self.prgm_ver = prgm_ver
        self.data = data
        if raw:
            self.raw = raw
        else:
            self._build_bytes()

    @property
    def type_name(self):
        """??????????????????????????????"""
        return self.TYPE_NAME_MAP.get(self.pkg_type, "TypeUnknown")

    def __str__(self):
        return """pkg_ver: {} pkg_type:{} prgm_ver:{} data:{}""".format(
            self.pkg_ver,
            self.type_name,
            self.prgm_ver,
            self.data,
        )

    def __repr__(self):
        return self.__str__()

    def _build_bytes(self):
        self.raw = struct.pack(
            self.FORMAT_PKG,
            self.pkg_ver,
            self.pkg_type,
            self.prgm_ver,
            self.data_encode(self.pkg_type, self.data),
        )

    @classmethod
    def _prebuilt_pkg(cls, pkg_type, fallback):
        """act as lru_cache"""
        if pkg_type not in cls._cache_prebuilt_pkg:
            pkg = fallback(force_rebuilt=True)
            cls._cache_prebuilt_pkg[pkg_type] = pkg

        return cls._cache_prebuilt_pkg[pkg_type]

    @classmethod
    def recalc_crc32(cls):
        cls.SECRET_KEY_CRC32 = binascii.crc32(SECRET_KEY.encode('utf-8')) & 0xffffffff
        cls.SECRET_KEY_REVERSED_CRC32 = binascii.crc32(SECRET_KEY[::-1].encode('utf-8')) & 0xffffffff

    @classmethod
    def data_decode(cls, ptype, data_raw):
        return struct.unpack(cls.FORMATS_DATA[ptype], data_raw)

    @classmethod
    def data_encode(cls, ptype, data):
        return struct.pack(cls.FORMATS_DATA[ptype], *data)

    def verify(self, pkg_type=None):
        try:
            if pkg_type is not None and self.pkg_type != pkg_type:
                return False
            elif self.pkg_type == self.PTYPE_HS_S2M:
                # Slaver-->Master ??????????????????
                return self.data[0] == self.SECRET_KEY_REVERSED_CRC32

            elif self.pkg_type == self.PTYPE_HEART_BEAT:
                # ??????
                return True

            elif self.pkg_type == self.PTYPE_HS_M2S:
                # Master-->Slaver ????????????
                return self.data[0] == self.SECRET_KEY_CRC32

            else:
                return True
        except:
            return False

    @classmethod
    def decode_only(cls, raw):
        """
        decode raw bytes to CtrlPkg instance, no verify
        use .decode_verify() if you also want verify

        :param raw: raw bytes content of package
        :type raw: bytes
        :rtype: CtrlPkg
        """
        if not raw or len(raw) != cls.PACKAGE_SIZE:
            raise ValueError("content size should be {}, but {}".format(
                cls.PACKAGE_SIZE, len(raw)
            ))
        pkg_ver, pkg_type, prgm_ver, data_raw = struct.unpack(cls.FORMAT_PKG, raw)
        data = cls.data_decode(pkg_type, data_raw)

        return cls(
            pkg_ver=pkg_ver, pkg_type=pkg_type,
            prgm_ver=prgm_ver,
            data=data,
            raw=raw,
        )

    @classmethod
    def decode_verify(cls, raw, pkg_type=None):
        """decode and verify a package
        :param raw: raw bytes content of package
        :type raw: bytes
        :param pkg_type: assert this package's type,
            if type not match, would be marked as wrong
        :type pkg_type: int

        :rtype: CtrlPkg, bool
        :return: tuple(CtrlPkg, is_it_a_valid_package)
        """
        try:
            pkg = cls.decode_only(raw)
        except:
            return None, False
        else:
            return pkg, pkg.verify(pkg_type=pkg_type)

    @classmethod
    def pbuild_hs_m2s(cls, force_rebuilt=False):
        """pkg build: Handshake Master to Slaver"""
        # because py27 do not have functools.lru_cache, so we must write our own
        if force_rebuilt:
            return cls(
                pkg_type=cls.PTYPE_HS_M2S,
                data=(cls.SECRET_KEY_CRC32,),
            )
        else:
            return cls._prebuilt_pkg(cls.PTYPE_HS_M2S, cls.pbuild_hs_m2s)

    @classmethod
    def pbuild_hs_s2m(cls, force_rebuilt=False):
        """pkg build: Handshake Slaver to Master"""
        if force_rebuilt:
            return cls(
                pkg_type=cls.PTYPE_HS_S2M,
                data=(cls.SECRET_KEY_REVERSED_CRC32,),
            )
        else:
            return cls._prebuilt_pkg(cls.PTYPE_HS_S2M, cls.pbuild_hs_s2m)

    @classmethod
    def pbuild_heart_beat(cls, force_rebuilt=False):
        """pkg build: Heart Beat Package"""
        if force_rebuilt:
            return cls(
                pkg_type=cls.PTYPE_HEART_BEAT,
            )
        else:
            return cls._prebuilt_pkg(cls.PTYPE_HEART_BEAT, cls.pbuild_heart_beat)

    @classmethod
    def recv(cls, sock, timeout=CTRL_PKG_TIMEOUT, expect_ptype=None):
        """just a shortcut function
        :param sock: which socket to recv CtrlPkg from
        :type sock: socket.SocketType
        :rtype: CtrlPkg,bool
        """
        buff = select_recv(sock, cls.PACKAGE_SIZE, timeout)
        pkg, verify = CtrlPkg.decode_verify(buff, pkg_type=expect_ptype)  # type: CtrlPkg,bool
        return pkg, verify
