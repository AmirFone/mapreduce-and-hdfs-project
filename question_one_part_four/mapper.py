#!/usr/bin/env python
import sys
import time

count = 0
for line in sys.stdin:
    if count:
        try:
            line = line.strip().split(",")
            # key=Summons Number, value=Vehicle Color
            print(line[0]+','+line[33].lower().replace(' ',''))
        # if count == 500:
        #     break
        except:
            continue
    count += 1
