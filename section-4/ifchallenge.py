"""
Completed the if challenge homework
"""
NAME = input("Please enter your name: ")
AGE = int(input("How old are you? "))

if 18 <= AGE < 31:
    print("Welcome club 18-30 holidays, {0}".format(NAME))
else:
    print("I'm sorry, our holidays are only for cool people")
