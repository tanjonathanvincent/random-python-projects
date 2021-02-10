# Last updated on 2020.11.29

import json

print("This is a test program for JSON\n")

number = input("Please input a number: ")
text = input("Please input the text: ")

jsonEntry = {
    "number": number,
    "text": text
}

json = json.dump(jsonEntry, indent=2, sort_keys=True)
print(json)
