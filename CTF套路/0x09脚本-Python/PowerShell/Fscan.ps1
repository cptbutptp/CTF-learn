Set-ExecutionPolicy bypass
$MyConsole = 'C:\Windows\SysWOW64\cmd.exe'
$computername = 'localhost'

write-host " "
write-host " _____   _____    _____   _____        ___     _____   _____   _____   _____   _____   _____        ___  ___       ___   __   _  "
write-host "|_   _| /  _  \  |  _  \ | ____|      /   |   |  _  \ | ____| |_   _| |_   _| | ____| |  _  \      /   |/   |     /   | |  \ | | " 
write-host "  | |   | | | |  | |_| | | |__       / /| |   | |_| | | |__     | |     | |   | |__   | |_| |     / /|   /| |    / /| | |   \| | "
write-host "  | |   | | | |  |  _  { |  __|     / / | |   |  _  { |  __|    | |     | |   |  __|  |  _  /    / / |__/ | |   / / | | | |\   | "
write-host "  | |   | |_| |  | |_| | | |___    / /  | |   | |_| | | |___    | |     | |   | |___  | | \ \   / /       | |  / /  | | | | \  | "
write-host "  |_|   \_____/  |_____/ |_____|  /_/   |_|   |_____/ |_____|   |_|     |_|   |_____| |_|  \_\ /_/        |_| /_/   |_| |_|  \_| "
write-host " "
write-host " "
write-host  "输入1 扫描开放端口"
write-host  "输入2 建立/删除防火墙策略"
write-host  "输入3 更改用户账号密码"
write-host  "输入4 管理员账号降权"
write-host  "输入5 移动/删除/查找文件目录"
write-host  "输入6 退出"
write-host " "
while(1){
	[int]$number = read-host "enter a num"
	Switch($number)
	{
		1{
			[string]$ip = read-host "RHOST"
            write-warning "请输入一个端口"
            $S_port = read-host "RPORT (默认为1-1024)"
            if($S_port){
                    $S_port | % {echo ((new-object Net.Sockets.TcpClient).Connect($ip,$_)) "Port $_ is open!"} 2>$null
                }
            else{
                1..5960 | % {echo ((new-object Net.Sockets.TcpClient).Connect($ip,$_)) "Port $_ is open!"} 2>$null
                continue;
            }
        }
        
		2{
			Write-Host "输入a 增加防火墙策略"
			Write-Host "输入b 删除防火墙策略"
			Write-Host "输入c 更改3389端口"

			[string]$firewall = Read-Host "请选择"
			Switch($firewall){
			a{
			#改变防火墙策略
				[string] $firewall_policy = read-host "Do  you want to change firewallpolicy?[Y/N]"
				if($firewall_policy -eq "y")
				{ 
					netsh advfirewall set allprofiles state on 1>$nulls
					Write-Host "防火墙已开启！" -ForegroundColor Red
					netsh advfirewall firewall add rule name="Allow Ping" dir=in protocol=icmpv4 action=block 1>$null
					netsh advfirewall firewall add rule name="FTP20" protocol=TCP dir=in localport=20 action=block 1>$null
					netsh advfirewall firewall add rule name="FTP21" protocol=TCP dir=in localport=21 action=block 1>$null
					netsh advfirewall firewall add rule name="SSH" protocol=TCP dir=in localport=22 action=block 1>$null
					netsh advfirewall firewall add rule name="Telnet" protocol=TCP dir=in localport=23 action=block 1>$null
					netsh advfirewall firewall add rule name="SMTP" protocol=TCP dir=in localport=25 action=block 1>$null
					netsh advfirewall firewall add rule name="TFTP" protocol=UDP dir=in localport=69 action=block 1>$null
					netsh advfirewall firewall add rule name="POP3" protocol=TCP dir=in localport=110 action=block 1>$null
					netsh advfirewall firewall add rule name="Netbios-ns" protocol=UDP dir=in localport=137 action=block 1>$null
					netsh advfirewall firewall add rule name="Netbios-dgm" protocol=UDP dir=in localport=138 action=block 1>$null
					netsh advfirewall firewall add rule name="Netbios-ssn" protocol=TCP dir=in localport=139 action=block 1>$null
					netsh advfirewall firewall add rule name="Netbios-ds" protocol=TCP dir=in localport=445 action=block 1>$null

					Write-Host "Ping have protection" -ForegroundColor Red
					Write-Host "FTP-20 have protection" -ForegroundColor Red
					Write-Host "FTP-21 have protection" -ForegroundColor Red
					Write-Host "SSH have protection" -ForegroundColor Red
					Write-Host "Telnet have protection" -ForegroundColor Red
					Write-Host "SMTP have protection" -ForegroundColor Red
					Write-Host "TFTP have protection" -ForegroundColor Red
					Write-Host "POP3 have protection" -ForegroundColor Red
					Write-Host "Netbios-ns have protection" -ForegroundColor Red
					Write-Host "Netbios-ssn have protection" -ForegroundColor Red
					Write-Host "Netbios-ds have protection" -ForegroundColor Red
					Write-Host "Netbios-dgm have protection" -ForegroundColor Red
				}
				else{"食屎啦你！还玩不玩啦! -_-|| "}
			}

			b{
                write-warning "请注意 该功能是用于删除本脚本所添加的策略"
                $delete = read-host "是否删除[Y/N]"
                if($delete -eq "y"){
				    netsh advfirewall firewall delete rule name=Allow Ping dir=in 1>$null
				    netsh advfirewall firewall delete rule name=FTP20 dir=in 1>$null
				    netsh advfirewall firewall delete rule name=FTP21 dir=in 1>$null
				    netsh advfirewall firewall delete rule name=SSH dir=in 1>$null
				    netsh advfirewall firewall delete rule name=Telnet dir=in 1>$null
				    netsh advfirewall firewall delete rule name=SMTP dir=in 1>$null
				    netsh advfirewall firewall delete rule name=TFTP dir=in 1>$null
				    netsh advfirewall firewall delete rule name=POP3 dir=in 1>$null
				    netsh advfirewall firewall delete rule name=Netbios-ns dir=in 1>$null
				    netsh advfirewall firewall delete rule name=Netbios-ssn dir=in 1>$null
				    netsh advfirewall firewall delete rule name=Netbios-ds dir=in 1>$null
				    netsh advfirewall firewall delete rule name=Netbios-dgm dir=in 1>$null
				    Write-Host "策略成功删除"
                }
                else{write-host "未删除策略" -fore yellow
                }
			}

			c{
				[string]$change_port = Read-Host "Do you want change 3889?[Y/N]"
				if($change_port -eq "y")
				{
					if($result.PrimaryStatus -eq '3389'){
						$portNumber = read-host "请设置任意端口号(1024-65530)"
						$original=Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name 'portnumber'
						Write-Host 当前RDP默认端口为$original.PortNumber
						$result=Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name 'portnumber' -Value $PortNumber
						Write-Host 已经完成 RDP 端口的修改！ -ForegroundColor Green
						Write-Host 正在重启 Remote Desktop Services ... -ForegroundColor DarkYellow
						Restart-Service termservice -Force
					}
				}
				else{
					write-host "Bye"
			        continue;
				}
			}

			}
		}
    
		3{
			$user = net user
			echo $user
			$C_user = Read-Host "请输入你想更改的用户名"
			$C_passwd = Read-Host "请输入密码"
			net user $C_user $C_passwd 1>$null
			write-host "更改成功" -ForegroundColor Yellow
			continue;
		}
		4{
			$Ad_user = net localgroup administrators
			Write-Host 您的管理员账户是
			$group = [ADSI]"WinNT://$env:COMPUTERNAME/administrators"
			$group.psbase.invoke("Members")|%{$_.GetType().InvokeMember("Name",'GetProperty',$null,$_,$null)}
			$policy = Read-Host "请输入要降权的用户名"
			net localgroup administrators $policy /del
			write-host "降权成功" -ForegroundColor Yellow
			continue;

		}
		5{
			Write-Host "输入a 更改文件目录"
			Write-Host "输入b 查找文件"

			[string]$CH_file = Read-Host "请选择"
			Switch($CH_file){
				a{
					$C_file = read-host "想更改的原文件目录"
					$file = read-host "想更改的目的文件目录"
					Move-Item -path $C_file\*  -destination $file
					[string]$choose = Read-Host "移动成功 是否删除源文件夹[Y/N]"
					if($choose -eq 'y'){
						del $C_file -Recurse
						Write-Host "删除成功"
					}
					else{Write-Host "未删除"}
						continue;
				}
				b{
					$dizhi = Read-Host "请输入查找地址"
					$filename = Read-Host "请输入文件名"
					Dir $dizhi -filter *$filename* -recurse 2>$null 
				}
			}	
        
		}

		6{Write-Host "Bye"
			exit;
		}
	}
}

