"""
This script explores more details about ranges
"""
DECIMALS = range(0, 100)
MY_RANGE = DECIMALS[3:40:3]
print(MY_RANGE == range(3, 40, 3))
print(range(0, 5, 2) == range(0, 6, 2))
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

RANGE = range(0, 100)
print(RANGE)

for index in RANGE[::-2]:
    print(index)

print("=" * 50)
for index in range(99, 0, -2):
    print(index)

print("=" * 50)
print(range(0, 100)[::-2] == range(99, 0, -2))

for index in range(0, 100, -2):
    print(index)
BACKSTRING = "egaugnal lufrewop yrev a si nohtyP"
print(BACKSTRING[::-1])

RANGE = range(0, 10)
for index in RANGE[::-1]:
    print(index)

LETTER_O = range(0, 100, 4)
print(LETTER_O)
P = LETTER_O[::5]
print(P)
for index in P:
    print(index)
