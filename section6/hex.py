"""
Hexadecimal and Octal and the Challenges
"""
for index in range(17):
    print("{0:>2} in hex is {0:02x}".format(index))

X = 0x20
Y = 0x0a
print(X)
print(Y)
print(X * Y)
print(0b101010)

POWERS = []
for power in range(15, -1, -1):
    POWERS.append(8 ** power)

print(POWERS)

X = int(input("Please enter a number: "))

PRINTING = False

for power in POWERS:
    bit = X // power
    if bit != 0 or power == 1:
        PRINTING = True
    if PRINTING:
        print(bit, end="")
    X %= power
