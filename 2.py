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

# helper function for my dumb human brain


def rockPaperTranslate(input):
    if input in ["A", "X"]:
        return "rock"
    elif input in ["B", "Y"]:
        return "paper"
    elif input in ["C", "Z"]:
        return "scisors"


def rockPaperScisors(player1, player2):
    game = "".join([player1, player2])
    if game in ["AZ", "BX", "CY"]:
        return "lose"
    elif game in ["AX", "BY", "CZ"]:
        return "tie"
    else:
        return "win"


def scoreGame(result):
    if result == "win":
        return 6
    elif result == "tie":
        return 3
    else:
        return 0


def scorePlay(play):
    if play in ["A", "X"]:
        return 1
    elif play in ["B", "Y"]:
        return 2
    else:
        return 3


score = 0

for index, game in enumerate(data):
    (player1, player2) = game.split(" ")
    result = rockPaperScisors(player1, player2)
    print(
        f"Game {index + 1}: {rockPaperTranslate(player1)} vs {rockPaperTranslate(player2)}: {result}")

    gameScore = scorePlay(player2) + scoreGame(result)
    print(f"Score: {gameScore}")
    score += gameScore

print(f"Total Score: {score}")
