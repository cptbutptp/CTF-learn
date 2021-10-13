
strGH="10684"
'输入工号
strLDAP = "LDAP://ou=用户,DC=winlandcn,DC=com"
'AD表名
Set objCn = CreateObject("ADODB.Connection")
Set objCmd =   CreateObject("ADODB.Command")
objCn.Provider = "ADsDSOObject"
objCn.Open "Active Directory Provider"
Set objCmd.ActiveConnection = objCn
'创建ADO连接
objCmd.Properties("Searchscope") = 2 
objCmd.CommandText = "SELECT displayName,telephoneNumber FROM '" & strLDAP & "' WHERE objectCategory='user' and sAMAccountName='"& strGH &"'"
Set objRs = objCmd.Execute


objRs.MoveFirst
Do Until objRs.EOF
     strTmp = Trim(objRs.Fields("displayName").Value & "")
     strTmp2 = Trim(objRs.Fields("telephoneNumber").Value & "")
     Wscript.Echo strtmp
     WScript.Echo strtmp2
     objRs.MoveNext
Loop
