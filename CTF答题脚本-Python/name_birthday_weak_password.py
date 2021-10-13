weak_password = ['000000', '0000000', '111111', '11111111', '112233', '123123', '123321', '123456', '12345678', '87654321', '123456789', '987654321', '1234567890', '0123456789', '654321', '666666', '888888', '666888',
                 '66668888', 'abcdef', '147258369', 'abcabc', 'abc123', 'a1b2c3', 'aaa111', '123qwe', 'qweasd', 'admin', 'root', 'pass123', 'p@ssword', 'password', 'passwd', 'iloveyou', '5201314', 'qq123456', 'taobao', 'wang1234']
foreign_weak_password = ['password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', '1234567', 'letmein', 'trustno1', 'dragon', 'baseball', '111111', 'iloveyou', 'master', 'sunshine', 'ashley', 'bailey', 'passw0rd',
                         'shadow', '123123', '654321', 'superman', 'qazwsx', 'michael', 'football', 'qwerty', 'welcome', 'ninja', 'hello', 'happy', 'anything', 'abcabcabc', 'qwert123', 'system', 'command', 'adminstrator', 'mouse', 'harddisk']
name = ['xiaoming', 'Xiaoming', 'xiaoMing',
        'xiao_ming', 'xiaoM', 'XMing', 'Xming', 'xl', 'XM']
birth = ['1995', '_1995', '09', '9', '23', '199509', '_950923', '_199509',
         '9509', '0923', '19950925', '1314', '520', '123', '123456', '888', '666']
day = ['1314', '520', '000', '111', '123', '168', '1234', '123456',
       '5201314', '888', '666', '123123', 'qwe', 'asd', 'zxc', 'aaa', ]
f = open('dir.txt', 'w')
for e in weak_password:
    f.write(e + '\n')
for g in foreign_weak_password:
    f.write(g + '\n')
for n in name:
    for b in birth:
        for b2 in birth:
            f.write(b2 + n + b + '\n')
            f.write(b2 + b + n + '\n')
            f.write(n + b2 + b + '\n')
for c in name:
    for d in day:
        f.write(c + d + '\n')
        f.write(d + c + '\n')
f.close()
