#!/usr/bin/env python
from os import path

with open("./data/1.txt", encoding='utf-8') as file:
    mostCals = 0
    currentCals = 0
    for line in file:
        if line == "\n":
            print(f"This Elf is carrying {currentCals}")
            if currentCals >= mostCals:
                mostCals = currentCals
            currentCals = 0
        else:
            currentCals = currentCals + int(line)
    
    print(f"The elf carrying the most calories is carrying {mostCals}")
