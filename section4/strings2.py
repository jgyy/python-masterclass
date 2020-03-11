"""
This is the seconds portion of string practice for section 4
"""
NUMBER = input("Please enter a series of numbers, using any separators you like:")
SEPERATORS = ""

for char in NUMBER:
    if not char.isnumeric():
        SEPERATORS += char
print(SEPERATORS)

VALUES = "".join(char if char not in SEPERATORS else " " for char in NUMBER).split()
print(sum([int(val) for val in VALUES]))
