# This program was last update on 2020.11.29

import json


# Overwrite existing JSON to reflect new entries
def writeJson(data):
    with open("dice.json", "w") as jsonNewFile:
        json.dump(data, jsonNewFile, indent=2, sort_keys=True)


with open("dice.json") as jsonFile:
    data = json.load(jsonFile)
    temp = data["diceware_old"]

    number = int(input("Enter the mumber to be deleted: "))

    for i in range(len(temp)):
        if temp[i]["number"] == number:
            del temp[i]
            break

writeJson(data)
