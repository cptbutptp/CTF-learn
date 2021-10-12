#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pysnmp.sf.net/license.html
#
# PySNMP MIB module PYSNMP-SOURCE-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///Users/ilya/src/py/pysnmp/docs/mibs/PYSNMP-SOURCE-MIB.txt
# Produced by pysmi-0.0.5 at Sat Sep 19 16:25:01 2015
# On host grommit.local platform Darwin version 14.4.0 by user ilya
# Using Python version 2.7.6 (default, Sep  9 2014, 15:04:36) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( pysnmpModuleIDs, ) = mibBuilder.importSymbols("PYSNMP-MIB", "pysnmpModuleIDs")
( snmpTargetAddrEntry, ) = mibBuilder.importSymbols("SNMP-TARGET-MIB", "snmpTargetAddrEntry")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TAddress, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TAddress", "TextualConvention")
pysnmpSourceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8)).setRevisions(("2015-01-16 00:00",))
if mibBuilder.loadTexts: pysnmpSourceMIB.setLastUpdated('201501160000Z')
if mibBuilder.loadTexts: pysnmpSourceMIB.setOrganization('SNMP Laboratories')
if mibBuilder.loadTexts: pysnmpSourceMIB.setContactInfo('E-mail:     info@snmplabs.com\n                  Subscribe:  pysnmp-users-request@lists.sourceforge.net')
if mibBuilder.loadTexts: pysnmpSourceMIB.setDescription('This MIB module defines implementation specific objects\n\t     that provide variable source transport endpoints feature to\n             SNMP Engine and Applications.')
pysnmpSourceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1))
pysnmpSourceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2))
snmpSourceAddrTable = MibTable((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1), )
if mibBuilder.loadTexts: snmpSourceAddrTable.setDescription('A table of transport addresses to be used as a source in the\n         generation of SNMP messages. This table contains additional\n         objects for the SNMP-TRANSPORT-ADDRESS::snmpSourceAddressTable.')
snmpSourceAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1, 1), )
snmpTargetAddrEntry.registerAugmentions(("PYSNMP-SOURCE-MIB", "snmpSourceAddrEntry"))
snmpSourceAddrEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts: snmpSourceAddrEntry.setDescription('A transport address to be used as a source in the generation\n         of SNMP operations.\n\n         An entry containing additional management information\n         applicable to a particular target.')
snmpSourceAddrTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 1, 1, 1, 1), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: snmpSourceAddrTAddress.setDescription('This object contains a transport address.  The format of\n         this address depends on the value of the\n         snmpSourceAddrTDomain object.')
pysnmpSourceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2, 1))
pysnmpSourceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1, 8, 2, 2))
mibBuilder.exportSymbols("PYSNMP-SOURCE-MIB", snmpSourceAddrTAddress=snmpSourceAddrTAddress, pysnmpSourceMIBGroups=pysnmpSourceMIBGroups, pysnmpSourceMIB=pysnmpSourceMIB, pysnmpSourceMIBConformance=pysnmpSourceMIBConformance, snmpSourceAddrTable=snmpSourceAddrTable, pysnmpSourceMIBCompliances=pysnmpSourceMIBCompliances, PYSNMP_MODULE_ID=pysnmpSourceMIB, pysnmpSourceMIBObjects=pysnmpSourceMIBObjects, snmpSourceAddrEntry=snmpSourceAddrEntry)
