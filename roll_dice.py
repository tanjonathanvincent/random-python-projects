# Last updated on 2020.11.28

from random import randint

roll = "yes"

while roll == "yes" or roll == "y":
    # Generates a random number
    # between 1 and 6
    number = randint(1, 6)
    print("Rolling the dice...")

    if number == 1:
        print("The value is 1")
    if number == 2:
        print("The value is 2")
    if number == 3:
        print("The value is 3")
    if number == 4:
        print("The value is 4")
    if number == 5:
        print("The value is 5")
    if number == 6:
        print("The value is 6")

    roll = "no"
    roll = input("Do you want to roll again? ")
    print("\n")
