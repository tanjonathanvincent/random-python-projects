# Last updated on: 2020.11.29

import json

print("This program will append entries in a JSON file\n")


# Function to add to JSON
def writeJson(data, filename="data/data2.json"):
    with open(filename, "w") as jsonNewFile:
        json.dump(data, jsonNewFile, indent=2, sort_keys=True)


number = input("Please input a number: ")
text = input("Please input the text: ")

with open("data/data.json") as jsonFile:
    data = json.load(jsonFile)

    jsonEntry = {
        "number": number,
        "text": text
    }

    data.append(jsonEntry)

writeJson(data)
