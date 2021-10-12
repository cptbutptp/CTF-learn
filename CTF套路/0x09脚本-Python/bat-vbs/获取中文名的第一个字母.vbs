Set objNetwork = CreateObject("Wscript.Network")
strComputer = objNetwork.ComputerName'获取当前的机器名
strUserName=objNetwork.UserName'获取当前的用户名
Set objLocalSam =GetObject("WinNT://" & strComputer & "/" & strUserName)'这里做了修改，scottlocke中默认strUserName为"Administrator"是不保险的
Wscript.echo SIDArray(objLocalSam.objectSID)
Function SIDArray(bar)
  ' Converts Binary Array into Human readable eg: S-1-5-21-XXXXX-XXXXX-XXXXX-XXX
  dim seperator,sid,length
  seperator = ""
  sid = ""
  for length = 1 to lenb(bar)
    sid = sid & seperator & right("0" & hex(ascb(midb(bar,length,1))),2)
    seperator = ","
  Next
  SIDArray = sid
  SID = Split(SIDArray,",")
' Convert into standard viewable format - little endian format for 4 byte groups
SID1 = (HexToDec(Mid(SID(15), 1, 1))*268435456) + (HexToDec(Mid(SID(15), 2, 2))*16777216) + (HexToDec(Mid(SID(14), 1, 1))*1048576) + (HexToDec(Mid(SID(14), 2, 2))*65536) + (HexToDec(Mid(SID(13), 1, 1))*4096) + (HexToDec(Mid(SID(13), 2, 2))*256) + (HexToDec(Mid(SID(12), 1, 1))*16) + HexToDec(Mid(SID(12), 2, 2))
SID2 = (HexToDec(Mid(SID(19), 1, 1))*268435456) + (HexToDec(Mid(SID(19), 2, 2))*16777216) + (HexToDec(Mid(SID(18), 1, 1))*1048576) + (HexToDec(Mid(SID(18), 2, 2))*65536) + (HexToDec(Mid(SID(17), 1, 1))*4096) + (HexToDec(Mid(SID(17), 2, 2))*256) + (HexToDec(Mid(SID(16), 1, 1))*16) + HexToDec(Mid(SID(16), 2, 2))
SID3 = (HexToDec(Mid(SID(23), 1, 1))*268435456) + (HexToDec(Mid(SID(23), 2, 2))*16777216) + (HexToDec(Mid(SID(22), 1, 1))*1048576) + (HexToDec(Mid(SID(22), 2, 2))*65536) + (HexToDec(Mid(SID(21), 1, 1))*4096) + (HexToDec(Mid(SID(21), 2, 2))*256) + (HexToDec(Mid(SID(20), 1, 1))*16) + HexToDec(Mid(SID(20), 2, 2))
RID = (HexToDec(Mid(SID(27), 1, 1))*268435456) + (HexToDec(Mid(SID(27), 2, 2))*16777216) + (HexToDec(Mid(SID(26), 1, 1))*1048576) + (HexToDec(Mid(SID(26), 2, 2))*65536) + (HexToDec(Mid(SID(25), 1, 1))*4096) + (HexToDec(Mid(SID(25), 2, 2))*256) + (HexToDec(Mid(SID(24), 1, 1))*16) + HexToDec(Mid(SID(24), 2, 2))
' Cheating here by just prepending the S-1-5-21-
SIDArray = "S-1-5-21-" & SID1 & "-" & SID2 & "-" & SID3 & "-" & RID
End Function
Function HexToDec(ByVal sHex)
HexToDec = "" & CLng("&H" & sHex)
End Function