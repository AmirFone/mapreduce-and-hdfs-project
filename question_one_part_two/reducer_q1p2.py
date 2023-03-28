#!/usr/bin/env python
import sys
dec_year = {}
dec_model = {}

for line in sys.stdin:
    line = line.strip().split(",")
    if len(line[1])>1 and len(line[2])>1:
        # aggregate by model
        if line[1] in dec_model:
            dec_model[line[1]] += 1
        else:
            dec_model[line[1]] = 1
        # aggregate by year
        if line[2] in dec_year:
            dec_year[line[2]] += 1
        else:
            dec_year[line[2]] = 1

# sort by most popular model
items = sorted(dec_model.items(), key=lambda x: x[1], reverse=True)
print(items[0])    
# sort by most popular year
items = sorted(dec_year.items(), key=lambda x: x[1], reverse=True)
print(items[0])