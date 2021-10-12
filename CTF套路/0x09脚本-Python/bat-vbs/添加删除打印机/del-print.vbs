on error resume next

Set WshNetwork = WScript.CreateObject("WScript.Network")
Set prints=wshnetwork.EnumPrinterConnections
For i = 1 To prints.Count - 1 Step 2
	WshNetwork.RemovePrinterConnection prints.Item(i)
Next