"""
Challenge to choose options from lists
"""
CHOICE = "-"
while CHOICE != "0":
    if CHOICE in "12345":
        print("You chose {}".format(CHOICE))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    CHOICE = input()
