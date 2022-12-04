#!/usr/bin/env python

import os
import string

dirname = os.path.dirname(__file__)

data = []
with open(os.path.join(dirname, "data/3.txt"), 'r') as file:
    data = [line.strip() for line in file.readlines()]

priortySum=0
for rucksack in data:
    half = int(len(rucksack)/2)
    commonItem = list(set(rucksack[:half]) & set(rucksack[-half:]))
    priority = string.ascii_letters.index(commonItem[0])+1
    print(f"Common item is {commonItem}, priorty {priority}")
    priortySum += priority

print(f"Total: {priortySum}")
    