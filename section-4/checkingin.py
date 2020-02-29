"""
This script practices on checking in conditions
"""
PARROT = "Norwegian Blue"

LETTER = input("Enter a character: ")

if LETTER in PARROT:
    print("{} is in {}".format(LETTER, PARROT))
else:
    print("I don;t need that letter")
