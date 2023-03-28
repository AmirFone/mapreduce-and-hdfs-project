#!/usr/bin/env python
import sys
Street_Name_dec = {}

for line in sys.stdin:
    line = line.strip().split(",")
    # key=Summons Number, value=Street Name
    # aggregate the values sent from mapper 
    if line[1] in Street_Name_dec:
        Street_Name_dec[line[1]] += 1
    else:
        Street_Name_dec[line[1]] = 1
    
# print the highest aggregated values
print(sorted(Street_Name_dec.items(), key=lambda x: x[1], reverse=True)[0])
