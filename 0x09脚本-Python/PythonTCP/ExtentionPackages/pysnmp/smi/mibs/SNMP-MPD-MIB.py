#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2016, Ilya Etingof <ilya@glas.net>
# License: http://pysnmp.sf.net/license.html
#
# PySNMP MIB module SNMP-MPD-MIB (http://pysnmp.sf.net)
# ASN.1 source file:///usr/share/snmp/mibs/SNMP-MPD-MIB.txt
# Produced by pysmi-0.0.5 at Sat Sep 19 16:31:46 2015
# On host grommit.local platform Darwin version 14.4.0 by user ilya
# Using Python version 2.7.6 (default, Sep  9 2014, 15:04:36) 
#
( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
( NotificationGroup, ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
( Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, ModuleIdentity, Gauge32, snmpModules, iso, ObjectIdentity, Bits, Counter32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "Gauge32", "snmpModules", "iso", "ObjectIdentity", "Bits", "Counter32")
( DisplayString, TextualConvention, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
snmpMPDMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 11)).setRevisions(("2002-10-14 00:00", "1999-05-04 16:36", "1997-09-30 00:00",))
if mibBuilder.loadTexts: snmpMPDMIB.setLastUpdated('200210140000Z')
if mibBuilder.loadTexts: snmpMPDMIB.setOrganization('SNMPv3 Working Group')
if mibBuilder.loadTexts: snmpMPDMIB.setContactInfo('WG-EMail:   snmpv3@lists.tislabs.com\n                  Subscribe:  snmpv3-request@lists.tislabs.com\n\n                  Co-Chair:   Russ Mundy\n                              Network Associates Laboratories\n                  postal:     15204 Omega Drive, Suite 300\n                              Rockville, MD 20850-4601\n                              USA\n\n                  EMail:      mundy@tislabs.com\n                  phone:      +1 301-947-7107\n\n                  Co-Chair &\n                  Co-editor:  David Harrington\n                              Enterasys Networks\n                  postal:     35 Industrial Way\n                              P. O. Box 5005\n                              Rochester NH 03866-5005\n                              USA\n                  EMail:      dbh@enterasys.com\n                  phone:      +1 603-337-2614\n\n                  Co-editor:  Jeffrey Case\n                              SNMP Research, Inc.\n                  postal:     3001 Kimberlin Heights Road\n                              Knoxville, TN 37920-9716\n                              USA\n                  EMail:      case@snmp.com\n                  phone:      +1 423-573-1434\n\n                  Co-editor:  Randy Presuhn\n                              BMC Software, Inc.\n                  postal:     2141 North First Street\n                              San Jose, CA 95131\n                              USA\n                  EMail:      randy_presuhn@bmc.com\n                  phone:      +1 408-546-1006\n\n                  Co-editor:  Bert Wijnen\n                              Lucent Technologies\n                  postal:     Schagen 33\n                              3461 GL Linschoten\n                              Netherlands\n                  EMail:      bwijnen@lucent.com\n                  phone:      +31 348-680-485\n                 ')
if mibBuilder.loadTexts: snmpMPDMIB.setDescription('The MIB for Message Processing and Dispatching\n\n                  Copyright (C) The Internet Society (2002). This\n                  version of this MIB module is part of RFC 3412;\n                  see the RFC itself for full legal notices.\n                 ')
snmpMPDAdmin = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 1))
snmpMPDMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2))
snmpMPDMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3))
snmpMPDStats = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 2, 1))
snmpUnknownSecurityModels = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownSecurityModels.setDescription('The total number of packets received by the SNMP\n                 engine which were dropped because they referenced a\n                 securityModel that was not known to or supported by\n                 the SNMP engine.\n                ')
snmpInvalidMsgs = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpInvalidMsgs.setDescription('The total number of packets received by the SNMP\n                 engine which were dropped because there were invalid\n                 or inconsistent components in the SNMP message.\n                ')
snmpUnknownPDUHandlers = MibScalar((1, 3, 6, 1, 6, 3, 11, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpUnknownPDUHandlers.setDescription('The total number of packets received by the SNMP\n                 engine which were dropped because the PDU contained\n                 in the packet could not be passed to an application\n                 responsible for handling the pduType, e.g. no SNMP\n                 application had registered for the proper\n                 combination of the contextEngineID and the pduType.\n                ')
snmpMPDMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 1))
snmpMPDMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 11, 3, 2))
snmpMPDCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 11, 3, 1, 1)).setObjects(*(("SNMP-MPD-MIB", "snmpMPDGroup"),))
if mibBuilder.loadTexts: snmpMPDCompliance.setDescription('The compliance statement for SNMP entities which\n                 implement the SNMP-MPD-MIB.\n                ')
snmpMPDGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 11, 3, 2, 1)).setObjects(*(("SNMP-MPD-MIB", "snmpUnknownSecurityModels"), ("SNMP-MPD-MIB", "snmpInvalidMsgs"), ("SNMP-MPD-MIB", "snmpUnknownPDUHandlers"),))
if mibBuilder.loadTexts: snmpMPDGroup.setDescription('A collection of objects providing for remote\n                 monitoring of the SNMP Message Processing and\n                 Dispatching process.\n                ')
mibBuilder.exportSymbols("SNMP-MPD-MIB", snmpMPDMIBObjects=snmpMPDMIBObjects, snmpMPDMIBCompliances=snmpMPDMIBCompliances, snmpMPDCompliance=snmpMPDCompliance, snmpMPDMIBGroups=snmpMPDMIBGroups, snmpMPDMIB=snmpMPDMIB, snmpMPDAdmin=snmpMPDAdmin, snmpInvalidMsgs=snmpInvalidMsgs, PYSNMP_MODULE_ID=snmpMPDMIB, snmpMPDStats=snmpMPDStats, snmpMPDMIBConformance=snmpMPDMIBConformance, snmpUnknownSecurityModels=snmpUnknownSecurityModels, snmpMPDGroup=snmpMPDGroup, snmpUnknownPDUHandlers=snmpUnknownPDUHandlers)
