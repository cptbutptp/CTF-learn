#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pysnmp.sf.net/license.html
#
# Copyright (C) 2008 Truelite Srl <info@truelite.it>
# Author: Filippo Giunchedi <filippo@truelite.it>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the BSD 2-Clause License as shipped with pysnmp.
#
# Description: twisted DatagramProtocol UDP transport
#
from pysnmp.carrier.twisted.dispatch import TwistedDispatcher
from pysnmp.carrier.base import AbstractTransport

class AbstractTwistedTransport(AbstractTransport):
    protoTransportDispatcher = TwistedDispatcher
    def __init__(self):
        self._writeQ = []
