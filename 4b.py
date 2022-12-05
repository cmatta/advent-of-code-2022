#!/usr/bin/env python

import os

dirname = os.path.dirname(__file__)

data = []
with open(os.path.join(dirname, "data/4.txt"), 'r', encoding='utf-8') as file:
    data = [line.strip().split(',') for line in file.readlines()]

count = 0

for pair in data:
    teamData = [[int(x) for x in team.split('-')] for team in pair]

    team1 = list(range(teamData[0][0], teamData[0][1]+1))
    team2 = list(range(teamData[1][0], teamData[1][1]+1))

    intersection = sorted(list(set(team1).intersection(team2)))

    if len(intersection) != 0:
        count += 1

print(count)
