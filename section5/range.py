"""
Understanding and using ranges
"""
MY_LIST = list(range(10))
print(MY_LIST)

EVEN = list(range(0, 1000, 2))
ODD = list(range(1, 1000, 2))

print(EVEN)
print(ODD)
MY_STRING = "abcdefghijklmnopqrstuvwxyz"
print(MY_STRING.index("e"))
print(MY_STRING[4])

SMALL_DECIMALS = range(0, 10)
print(SMALL_DECIMALS)

print(SMALL_DECIMALS.index(3))

print(ODD)

print(ODD[985])

SEVENS = range(7, 1000000, 7)
X = int(input("Please enter a positive number less than one million: "))
if X in SEVENS:
    print("{} is divisible by seven".format(X))

print(SMALL_DECIMALS)

MY_RANGE = SMALL_DECIMALS[::2]
print(MY_RANGE)
print(MY_RANGE.index(4))
DECIMALS = range(0, 100)
print(DECIMALS)

MY_RANGE = DECIMALS[3:40:3]
print(MY_RANGE)

for index in MY_RANGE:
    print(index)

print("=" * 40)

for index in range(3, 40, 3):
    print(index)

print(MY_RANGE == range(3, 40, 3))
