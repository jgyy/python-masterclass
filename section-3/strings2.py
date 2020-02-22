"""
This is the seconds portion of string practice
"""
PARROT = "Norwegian Blue"

print(PARROT[0:6:2])  # Nre
print(PARROT[0:6:3])  # Nw

NUMBER = "9,223;372:036 854,775;807"
SEPERATORS = NUMBER[1::4]
print(SEPERATORS)
VALUES = "".join(char if char not in SEPERATORS else " " for char in NUMBER).split()
print([int(val) for val in VALUES])
