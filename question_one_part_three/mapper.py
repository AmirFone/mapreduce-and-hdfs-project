#!/usr/bin/env python
import sys
import time

count = 0
for line in sys.stdin:
    if count:
        try:
            line = line.strip().split(",")
            # key=Summons Number, value=Street Name
            print(line[0]+','+line[24].lower().replace(' ',''))
        # if count == 1000:
        #     break
        except:
            continue
    count += 1
