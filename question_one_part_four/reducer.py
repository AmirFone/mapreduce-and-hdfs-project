#!/usr/bin/env python
import sys
Color = {}

for line in sys.stdin:
    line = line.strip().split(",")
    # key=Summons Number, value=Vehicle Color
    # aggregate the values sent from mapper 
    if line[1] in Color:
        Color[line[1]] += 1
    else:
        Color[line[1]] = 1
    
# print the highest aggregated values
print(sorted(Color.items(), key=lambda x: x[1], reverse=True)[0])


