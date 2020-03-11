"""
This script writes A guessing game
"""
import random

HIGHEST = 9999
ANSWER = random.randint(1, HIGHEST)
GUESS = 0  # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(HIGHEST))

while GUESS != ANSWER:
    GUESS = int(input())

    if GUESS == 0:
        break
    if GUESS == ANSWER:
        print("You got the answer correct.")
        break
    else:
        if GUESS < ANSWER:
            print("Please guess higher")
        else:  # guess must be greater than answer
            print("Please guess lower")
