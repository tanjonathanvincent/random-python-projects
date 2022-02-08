# Last updated on 2020.11.29

import json

print("This program will write a single entry in a JSON file\n")

number = input("Please input a number: ")
text = input("Please input the text: ")

jsonEntry = {
    "number": number,
    "text": text
}

with open("data/data.json", "w") as jsonFile:
    json.dump(jsonEntry, jsonFile, indent=2, sort_keys=True)
