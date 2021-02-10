# Last updated on 2020.10.10

import hashlib


# Encode function
def hashEncode():
    # Hashlib encodes user input so that it
    # will be accepted by MD5
    rawText = input("Enter text to be hashed: ")
    result = hashlib.md5(rawText.encode())

    # Using hexdigest(), the equivalent MD5 hash
    # is printed
    print("The md5 hash: ", end="")
    print(result.hexdigest())
    print('\n')


# Choice array
confirm = ["Yes", "yes", "Y", "y"]
notConfirm = ["No", "no", "N", "n"]


print("Simple MD5 hash encoder")
print("Last updated: Oct. 10, 2020\n\n")

# Initial encode
hashEncode()

# Loop wrapper
while True:
    # Encoding loop
    while True:
        choice = input("Do you want to convert again? (y/n): ")
        # If the user chooses to confirm, the program
        # will re-loop to encode MD5
        if choice in confirm:
            hashEncode()
        # If the user chooses to exit, the program will end
        elif choice in notConfirm:
            input("\nPress the Enter key to exit..")
            break
        # If the user inputs an unknown character, the program
        # will prompt to input the correct choice
        else:
            print("Invalid! Please try again.")
    break
