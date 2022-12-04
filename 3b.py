#!/usr/bin/env python

import os
import string

dirname = os.path.dirname(__file__)

data = []
with open(os.path.join(dirname, "data/3.txt"), 'r') as file:
    data = [line.strip() for line in file.readlines()]

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

priortySum=0
for group in chunks(data, 3):
    commonItem = list(set(group[0]) & set(group[1]) & set(group[2]))
    print(f"Common Item in {group}: {commonItem}")
    priority = string.ascii_letters.index(commonItem[0])+1
    print(f"Common item is {commonItem}, priorty {priority}")
    priortySum += priority

print(f"Total: {priortySum}")
    