#coding uft-8
#a需要和n互质，如果跑不出来，调整range
a=3;
n=26;
for i in range(100):
    if i*a%n==1:
        print i
        break