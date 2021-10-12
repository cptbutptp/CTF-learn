#!/usr/bin/env python

import base64
import re
from itertools import combinations

s=list('R2LMDEZVCKJHC2VJC0TLEQ')

for i in range(len(s)):
    for j in list(combinations([x for x in range(len(s))], i)):
        
        #c = list(combinations([x for x in range(len(s))], i))
        a=list(s)
        #print c 
        
        for k in j:
            a[k]= a[k].lower()

        r=repr(base64.b64decode(''.join(a)))
        
        if '\\x' not in r:
            print r[1:-1]