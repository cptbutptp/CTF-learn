#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pysnmp.sf.net/license.html
#
MibScalarInstance, = mibBuilder.importSymbols('SNMPv2-SMI', 'MibScalarInstance')

vacmViewSpinLock, = mibBuilder.importSymbols('SNMP-VIEW-BASED-ACM-MIB', 'vacmViewSpinLock')

__vacmViewSpinLock = MibScalarInstance(vacmViewSpinLock.name, (0,), vacmViewSpinLock.syntax)

mibBuilder.exportSymbols(
    "__SNMP-VIEW-BASED-ACM-MIB",
    vacmViewSpinLock = __vacmViewSpinLock
)
