#!/usr/bin/env python
import os
import itertools
from functools import cmp_to_key

dirname = os.path.dirname(__file__)

dataPart1 = []

with open(os.path.join(dirname, "data/13.txt"), 'r', encoding='utf-8') as file:
    dataPart1 = [l.split() for l in file.read().split('\n\n')]

def compare(left, right):
    if type(left) == int and type(right) == int:
        if left == right: 
            return None
        else:
            if left < right:
                return -1
            elif left > right:
                return 1
    elif type(left) == list and type(right) == list:
        for (l, r) in itertools.zip_longest(left, right):
            result = compare(l, r)
            if result is not None:
                return result
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right) 
    elif left is None and right is not None:
        return -1
    elif left is not None and right is None:
        return 1
    
                

correctPairs = []

for i, (packet1, packet2) in enumerate(dataPart1):
    first = eval(packet1)
    second = eval(packet2)

    if compare(first, second) == -1:
        correctPairs.append(i+1)

print(f"Part 1: {sum(correctPairs)}")

dataPart2 = [eval(x) for x in itertools.chain.from_iterable(dataPart1)]
dataPart2.append([[2]])
dataPart2.append([[6]])

sortedDataPart2 = sorted(dataPart2, key=cmp_to_key(compare))

print(f"Part 2: {(sortedDataPart2.index([[2]]) + 1) * (sortedDataPart2.index([[6]]) + 1)}")