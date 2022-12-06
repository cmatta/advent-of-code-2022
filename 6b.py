#!/usr/bin/env python
import os
from collections import deque

dirname = os.path.dirname(__file__)

data = []
with open(os.path.join(dirname, "data/6-test.txt"), 'r') as file:
    data = [line.strip() for line in file.readlines()]

buffer = deque([], 14)

for index, char in enumerate(data[0]):
    buffer.append(char)
    if len(buffer) == 14:
        if len(set(buffer)) == 14:
            print(index + 1)
            break
