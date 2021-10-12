filename=raw_input('enter file name:')  
f=open(filename,'rb')  

for i in range(0,16):  
    print "%3s" % hex(i) ,  
print  
for i in range(0,16):  
    print "%-3s" % "#" ,  
print  
f.seek(1104,0)  
index=0  

while True:  
    temp=f.read(1)  
    if len(temp) == 0:  
        break  
    else:  
        print "%3s" % temp.encode('hex'),  
        index=index+1  
    if index == 16:  
        index=0  
        print   
f.close() 