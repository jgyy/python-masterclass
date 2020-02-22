"""
This script writes A guessing game
"""
ANSWER = 5

print("Please guess number between 1 and 10: ")
GUESS = int(input())

if GUESS == ANSWER:
    print("You got it first time")
else:
    if GUESS < ANSWER:
        print("Please guess higher")
    else:  # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if GUESS == ANSWER:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly")


# if GUESS < ANSWER:
#     print("Please guess higher")
#     guess = int(input())
#     if GUESS == ANSWER:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif GUESS > ANSWER:
#     print("Please guess lower")
#     guess = int(input())
#     if GUESS == ANSWER:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it the first time.")
