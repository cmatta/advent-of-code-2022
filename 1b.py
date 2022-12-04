#!/usr/bin/env python
import os
from collections import deque

dirname = os.path.dirname(__file__)

with open(os.path.join(dirname, "./data/1.txt"), 'r') as file:
    elfCals = []
    currentCals = 0
    for line in file:
        if line == "\n":
            elfCals.append(currentCals)
            currentCals = 0
        else:
            currentCals = currentCals + int(line)
    
    print(f"There are {len(elfCals)} elves.")
    print(f"Sum of top three calories: {sum(sorted(elfCals, reverse=True)[:3])}")