"""
Script that learns about operators
"""
NUM_A = 12
NUM_B = 3

print(NUM_A + NUM_B)  # 15
print(NUM_A - NUM_B)  # 9
print(NUM_A * NUM_B)  # 3
print(NUM_A / NUM_B)  # 4.0
print(NUM_A // NUM_B)  # 4 integer division, rounded down towards minus infinity
print(NUM_A % NUM_B)  # 0 modulus: the remainder after integer division

print()

print(NUM_A + NUM_B / 3 - 4 * 12)
print(NUM_A + (NUM_B / 3) - (4 * 12))
print((((NUM_A + NUM_B) / 3) - 4) * 12)
print(((NUM_A + NUM_B) / 3 - 4) * 12)

NUM_C = NUM_A + NUM_B
NUM_D = NUM_C / 3
NUM_E = NUM_D - 4
print(NUM_E * 12)

print()

print(NUM_A / (NUM_B * NUM_A) / NUM_B)
