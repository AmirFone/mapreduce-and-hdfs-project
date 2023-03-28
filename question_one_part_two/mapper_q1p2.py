#!/usr/bin/env python
import sys
import time
count =0    
for line in sys.stdin:
    if count:
        try:
            line = line.strip().split(",")
            # key = line[0] value = line[35] and line[7]
            print(line[0]+','+line[35]+','+line[7].lower())
        except:
            print('error')
            continue
    # if count==100:
    #     break
    count+=1

