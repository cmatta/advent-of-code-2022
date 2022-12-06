#!/usr/bin/env python

import os
import re

dirname = os.path.dirname(__file__)

stacks = []
instructions = []

# read initial position
with open(os.path.join(dirname, "data/5-stacks.txt"), 'r', encoding='utf-8') as file:
    for line in file.readlines():
        row = []
        for column in [line[i:i+4] for i in range(0, len(line), 4)]:
            if column[0] == '[':
                row.append(column[1])
            else:
                row.append(None)
        stacks.append(row)

pivotedStacks = [list(filter(lambda x: x is not None, col)) for col in list(zip(*stacks[::-1]))]

# read instructions
numberMatcher = re.compile(r"^move (\d+) from (\d) to (\d)$")
with open(os.path.join(dirname, "data/5-instructions.txt"), 'r', encoding='utf-8') as file:
    for line in file.readlines():
        instructions.append([int(x) for x in numberMatcher.match(line.strip()).groups()])
        print(f"{line}: {instructions[-1]}")

for instruction in instructions:
    move = instruction[0]
    start = instruction[1] - 1
    end = instruction[2] - 1

    crane = pivotedStacks[start][-move:]
    pivotedStacks[start] = pivotedStacks[start][:len(pivotedStacks[start]) - move]
    pivotedStacks[end].extend(crane)

    

print("".join([y[-1] for y in pivotedStacks]))