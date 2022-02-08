# Last updated 2020.12.03

import json

again = "yes"


def tryInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def dictionary(userInput):
    switch = {
        1: "diceware_old",
        2: "eff_general_short_wordlist",
        3: "eff_long_wordlist",
        4: "eff_short_wordlist"
    }
    return switch.get(userInput, "Invalid choice!")


print("Diceware Lookup\n")
print("Please select a dictionary set to lookup on:")
print("1. Diceware Old")
print("2. EFF General Short Wordlist")
print("3. EFF Long Wordlist")
print("4. EFF Short Wordlist\n")
i = int(input("Please select your choice: "))
print("\n")

while again == "yes" or again == "y":
    with open("dice.json") as jsonFile:
        data = json.load(jsonFile)
        items = data[dictionary(userInput=i)]

        if i == 1:
            print("You are currently looking at the Diceware Old passphrases\n")
        elif i == 2:
            print("You are currently looking at the EFF General Short Wordlist\n")
        if i == 3:
            print("You are currently looking at the EFF Long Wordlist\n")
        if i == 4:
            print("You are currently looking at the EFF Short Wordlist\n")

        number = int(input("Please input the number: "))

        if tryInt(number) == True:
            for i in range(len(items)):
                if items[i]["number"] == number:
                    print("The text is: " + items[i]["text"])
        else:
            print("Not found! You probably entered a string?")

        again = "no"
        again = input("Search for another or try again? (y/n): ")
        print("\n")
