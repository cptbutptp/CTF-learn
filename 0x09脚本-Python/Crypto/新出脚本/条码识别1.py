from PIL import Image

def clean(img):
    A = img.load()
    ss = ''
    for x in xrange(img.size[0]):  
        ss += str(A[x, 10])
    ls = []
    while len(ss) > 0: 
        start = ss[0]
        j = 1
        while j < len(ss) and ss[j] == start :
            j += 1
        ls.append(j)
        ss = ss[j:]           
    return ls

def GetUPC_A(t):
    t = t[4:-4]
    for i in xrange(len(t)):
        t[i] = (t[i] + 1) / 4
    t = t[:24] + t[29:]
    s = ''
    for i in xrange(len(t)):
      s += str(t[i]) 
    upca = ''
    for i in range(0, len(s) / 4):
        n = i * 4
        upca += dic[s[n:n + 4]]     
    print upca

dic = {'3211':'0', '2221':'1', '2122':'2', '1411':'3', '1132':'4', '1231':'5', '1114':'6', '1312':'7', '1213':'8', '3112':'9'}
img = Image.open('7.png')  
GetUPC_A(clean(img))