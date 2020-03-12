"""
This section practice on lists
"""
# IP_ADDRESS = input("Please enter an IP address: ")
# print(IP_ADDRESS.count("."))
PARROT_LIST = ["non pinin", "no more", "a stiff", "be", "A Norwegian Blue"]

for state in PARROT_LIST:
    print("This parrot is " + state)

EVEN = [2, 4, 6, 8]
ODD = [1, 3, 5, 7, 9]

NUMBERS = EVEN + ODD
NUMBERS_IN_ORDER = sorted(NUMBERS)
print(NUMBERS_IN_ORDER)

if NUMBERS == NUMBERS_IN_ORDER:
    print("The lists are equal")
else:
    print("The lists are not equal")

if NUMBERS_IN_ORDER == sorted(NUMBERS):
    print("The lists are equal")
else:
    print("The lists are not equal")
