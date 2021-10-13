On Error Resume Next
 
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
  & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colNicConfigs = objWMIService.ExecQuery _
  ("SELECT * FROM Win32_NetworkAdapterConfiguration WHERE IPEnabled = True")
For Each objNicConfig In colNicConfigs    
   If Not objNicConfig.DHCPEnabled Then     
        intReturn = objNicConfig.EnableDHCP
        intReturn2=objNicConfig.SetDNSServerSearchOrder(Null)
    End If
Next

