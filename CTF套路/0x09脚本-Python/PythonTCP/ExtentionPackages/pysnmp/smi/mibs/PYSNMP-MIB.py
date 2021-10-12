#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pysnmp.sf.net/license.html
#
# PySNMP MIB module PYSNMP-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///Users/ilya/src/py/pysnmp/docs/mibs/PYSNMP-MIB.txt
# Produced by pysmi-0.0.5 at Sat Sep 19 16:21:43 2015
# On host grommit.local platform Darwin version 14.4.0 by user ilya
# Using Python version 2.7.6 (default, Sep  9 2014, 15:04:36) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pysnmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 20408)).setRevisions(("2005-05-14 00:00",))
if mibBuilder.loadTexts: pysnmp.setLastUpdated('200505140000Z')
if mibBuilder.loadTexts: pysnmp.setOrganization('pysnmp.sf.net')
if mibBuilder.loadTexts: pysnmp.setContactInfo('email: ilya@glas.net')
if mibBuilder.loadTexts: pysnmp.setDescription('Top-level infrastructure of the PySNMP project enterprise MIB tree')
pysnmpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 1))
pysnmpExamples = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 2))
pysnmpEnumerations = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3))
pysnmpModuleIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 1))
pysnmpAgentOIDs = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 2))
pysnmpDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 3, 3))
pysnmpExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 9999))
pysnmpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 4))
pysnmpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 4, 0))
pysnmpNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 4, 1))
pysnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 5))
pysnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 5, 1))
pysnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 20408, 5, 2))
mibBuilder.exportSymbols("PYSNMP-MIB", pysnmpAgentOIDs=pysnmpAgentOIDs, pysnmpNotificationPrefix=pysnmpNotificationPrefix, pysnmpModuleIDs=pysnmpModuleIDs, pysnmpGroups=pysnmpGroups, pysnmpCompliances=pysnmpCompliances, pysnmp=pysnmp, PYSNMP_MODULE_ID=pysnmp, pysnmpNotificationObjects=pysnmpNotificationObjects, pysnmpExamples=pysnmpExamples, pysnmpConformance=pysnmpConformance, pysnmpObjects=pysnmpObjects, pysnmpEnumerations=pysnmpEnumerations, pysnmpDomains=pysnmpDomains, pysnmpExperimental=pysnmpExperimental, pysnmpNotifications=pysnmpNotifications)
