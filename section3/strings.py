"""
This script is to practice scripts
"""
print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + "world")
GREETING = "Hello"
NAME = "JEff"
print(GREETING + NAME)

# if we want a space, we can add that too
print(GREETING + ' ' + NAME)

AGE = 24
print(AGE)

print(type(GREETING))
print(type(AGE))

AGE_IN_WORDS = "2 years"
print(NAME + f" is {AGE} years old")
print(type(AGE_IN_WORDS))

print(f"Pi is approximately {22 / 7:12.50f}")
PIE = 22 / 7
print(f"Pi is approximately {PIE:12.50f}")
