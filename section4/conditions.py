"""
This script is to practice on conditions
"""
AGE = int(input("How old are you? "))

if AGE in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if AGE < 16 or AGE > 65:
    print("Enjoy your free time")