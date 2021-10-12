@echo off
powercfg /create winland
powercfg /change winland /monitor-timeout-ac 15
powercfg /change winland /disk-timeout-ac 0
powercfg /change winland /standby-timeout-ac 60
powercfg /change winland /hibernate-timeout-ac 0
powercfg /setactive winland