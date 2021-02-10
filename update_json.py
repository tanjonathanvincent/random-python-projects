# Last updated on: 2020.11.29

import json


# Overwrite existing JSON to reflect new entries
def writeJson(data):
    with open("dice.json", "w") as newJsonFile:
        json.dump(data, newJsonFile, indent=2, sort_keys=True)


def tryInt(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


# Dictionery switcher
def dictionary(i):
    switch = {
        1: "diceware_old",
        2: "eff_general_short_wordlist",
        3: "eff_long_wordlist",
        4: "eff_short_wordlist"
    }
    return switch.get(i, "Invalid choice")


def updateEntry():
    again = "yes"

    print("Diceware Updater\n")
    print("Please select a dictionary set to update:")
    print("1. Diceware Old")
    print("2. EFF General Short Wordlist")
    print("3. EFF Long Wordlist")
    print("4. EFF Short Wordlist\n")
    i = int(input("Please select your choice: "))
    print("\n")

    while again == "yes" or again == "y":
        with open("dice.json") as jsonFile:
            data = json.load(jsonFile)
            temp = data[dictionary(i)]

            if i == 1:
                print("You are currently editing the Diceware Old list\n")
            elif i == 2:
                print("You are currently editing the EFF General Short Wordlist\n")
            elif i == 3:
                print("You are currently editing the EFF Long Wordlist\n")
            elif i == 4:
                print("You are currently editing the EFF Short Wordlist\n")

            number = input("Please input the number: ")
            text = input("Please input the text: ")

            if tryInt(number) == True:
                jsonEntry = {
                    "number": number,
                    "text": text
                }

                temp.append(jsonEntry)

                writeJson(data)
            else:
                print(
                    "Your entry was not recorded because the number you entered was a string!")

        again = "no"
        again = input("Add another entry or try again? (y/n): ")
        print("\n")
