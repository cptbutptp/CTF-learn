on error resume next
Dim WshNetwork
Set WshNetwork = WScript.CreateObject("WScript.Network")
WshNetwork.AddWindowsPrinterConnection "\\dc2\興美辦公室一體機(HP3052)","興美辦公室一體機(HP3052)"
WshNetwork.AddWindowsPrinterConnection "\\dc2\二樓激光黑白打印機(HP5100)","二樓激光黑白打印機(HP5100)"
WshNetwork.AddWindowsPrinterConnection "\\dc2\四樓震旦(僅黑白)打印機(ADC258)","四樓震旦(僅黑白)打印機(ADC258)"
WshNetwork.AddWindowsPrinterConnection "\\dc2\二樓震旦黑白打印機(AD258)","二樓震旦黑白打印機(AD258)"
WshNetwork.AddWindowsPrinterConnection "\\dc2\四樓震旦(僅彩色)打印機(ADC258)","四樓震旦(僅彩色)打印機(ADC258)"
WshNetwork.AddWindowsPrinterConnection "\\dc2\創意辦公室一體機(HP M1522)","創意辦公室一體機(HP M1522)"
WshNetwork.AddWindowsPrinterConnection "\\bg-pr-admin\威樂生產辦公室黑白激光打印機(HP1020)","威樂生產辦公室黑白激光打印機(HP1020)"
WshNetwork.AddWindowsPrinterConnection "\\wg-ac-009\二樓威樂財務部黑白激光打印機(HP1020)","二樓威樂財務部黑白激光打印機(HP1020)"
WshNetwork.AddWindowsPrinterConnection "\\bg-ship-admin\四樓船務部黑白打印機(HP1160)","四樓船務部黑白打印機(HP1160)"
WshNetwork.AddWindowsPrinterConnection "\\bg-ship-admin\四樓船務部彩色打印機(canon ip5200r)","四樓船務部彩色打印機(canon ip5200r)"
WshNetwork.AddWindowsPrinterConnection "\\wg-ac-011\四樓財務部黑白激光打印機(HP1020)","四樓財務部黑白激光打印機(HP1020)"
WshNetwork.AddWindowsPrinterConnection "\\wg-ac-014\四樓財務部黑白激光打印機(Canon LBP2900)","四樓財務部黑白激光打印機(Canon LBP2900)"
WshNetwork.AddWindowsPrinterConnection "\\ck-ma-002\一樓佧邦崎彩色噴墨打印機(EPSON R270)","WshNetwork.AddWindowsPrinterConnection "
WshNetwork.AddWindowsPrinterConnection "\\bg-mc-006\二樓物流部黑白激光打印機(HP2100)","二樓物流部黑白激光打印機(HP2100)"
WshNetwork.AddWindowsPrinterConnection "\\bg-mc-002\二樓物流部黑白激光打印機(HP1020)","二樓物流部黑白激光打印機(HP1020)"
WshNetwork.AddWindowsPrinterConnection "\\ck-de-003\CK(HP1020)","CK(HP1020)"
WshNetwork.AddWindowsPrinterConnection "\\xm-of-003\興美辦公室黑白激光打印機(Canon LBP2900)","興美辦公室黑白激光打印機(Canon LBP2900)"
WshNetwork.AddWindowsPrinterConnection "\\xm-of-005\興美辦公室針式打印機(Epson LQ-300K)","興美辦公室針式打印機(Epson LQ-300K)"



