from PIL import Image
import binascii
import itertools
import struct
import sys
import zlib


def read_chunk(f):
    length_bytes = f.read(4)
    if len(length_bytes) == 0:
        return None
    length = struct.unpack('>I', length_bytes)[0]
    blkname = f.read(4)
    data = f.read(length)
    crc = f.read(4)
    assert struct.pack('>I', binascii.crc32(blkname + data)) == crc
    return blkname, data, length_bytes + blkname + data + crc


with open('odrrere-start.png', 'rb') as f:
    with open('odrrere1.png', 'wb') as out:
        out.write(f.read(8))
        _, hdr, raw = read_chunk(f)
        out.write(raw)
        blocks = []
        end = None
        while True:
            chunk = read_chunk(f)
            if chunk is None:
                break
            blk, data, raw = chunk
            if blk == b'IDAT':
                blocks.append(raw)
            elif blk == b'IEND':
                end = raw
            else:
                out.write(raw)
        for c in sys.argv[1]:
            print(c)
            out.write(blocks['0123456789abc'.index(c)])
        out.write(end)