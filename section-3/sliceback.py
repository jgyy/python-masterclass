"""
This script focus on practicing slicing back
"""
LETTERS = "abcdefghijklmnopqrstuvwxyz"

BACKWARDS = LETTERS[::-1]
print(BACKWARDS)

# create a slice that produces the characters qpo
print(LETTERS[16:13:-1])

# slice the string to produce edcba
print(LETTERS[4::-1])

# slice the string to produce the last 8 characters, in reverse order
print(LETTERS[:-9:-1])

print(LETTERS[-4:])
print(LETTERS[-1:])
print(LETTERS[:1])
print(LETTERS[0])
