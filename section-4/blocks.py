"""
This script shows the for code block
"""
NAME = input("Please enter your name: ")
AGE = int(input("How old are you, {0}? ".format(NAME)))
print(AGE)

# if AGE >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - AGE))

if AGE < 18:
    print("Please come back in {0} years".format(18 - AGE))
elif AGE == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
