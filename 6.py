#!/usr/bin/env python
import os
from collections import deque

dirname = os.path.dirname(__file__)

data = []
with open(os.path.join(dirname, "data/6-test.txt"), 'r') as file:
    data = [line.strip() for line in file.readlines()]

buffer = deque([], 4)

for index, char in enumerate(data[0]):
    buffer.append(char)
    if len(buffer) == 4:
        if len(set(buffer)) == 4:
            print(index + 1)
            break
