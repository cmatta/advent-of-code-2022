#!/usr/bin/env python
# A🪨X
# B📄Y
# C✂️Z
#
import os

dirname = os.path.dirname(__file__)

data = []
with open(os.path.join(dirname, "data/2.txt"), 'r') as file:
    data = [line.strip() for line in file.readlines()]

win = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

lose = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

scoreGame = {
    "win": 6,
    "tie": 3,
    "lose": 0
}

scorePlay = {
    "A": 1,
    "B": 2,
    "C": 3
}

result = {
    "X": "lose",
    "Y": "tie",
    "Z": "win"
}


def rockPaperScisorsResult(player1, resultNeeded):
    if result[resultNeeded] == "tie":
        return player1
    if result[resultNeeded] == "win":
        return win[player1]
    if result[resultNeeded] == "lose":
        return lose[player1]
    

score = 0

for index, game in enumerate(data):
    (player1, resultNeeded) = game.split(" ")
    play = rockPaperScisorsResult(player1, resultNeeded)
    gameScore = scorePlay[play] + scoreGame[result[resultNeeded]]
    score += gameScore

print(f"Total Score: {score}")
