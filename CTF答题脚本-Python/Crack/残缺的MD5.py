import hashlib

str_src=list('TASC?O3RJMV?WDJKX?ZM')
str_md5='e9032'
str_list=list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ')
for i in range(len(str_list)):
    str_src[4]=str_list[i]
    for j in range(len(str_list)):
        str_src[11]=str_list[j]
        for z in range(len(str_list)):
            str_src[17]=str_list[z]
            stry_md5=str(hashlib.md5(''.join(str_src)).hexdigest())
            if stry_md5[:5] == str_md5:
                print ''.join(str_src),stry_md5