
strGH="10684"
'���빤��
strLDAP = "LDAP://ou=�û�,DC=winlandcn,DC=com"
'AD����
Set objCn = CreateObject("ADODB.Connection")
Set objCmd =   CreateObject("ADODB.Command")
objCn.Provider = "ADsDSOObject"
objCn.Open "Active Directory Provider"
Set objCmd.ActiveConnection = objCn
'����ADO����
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
