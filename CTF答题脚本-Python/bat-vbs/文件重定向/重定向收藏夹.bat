reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders" /v "Favorites" /t "REG_EXPAND_SZ" /d "d:\UserFiles\%username%\Favorites" /f
