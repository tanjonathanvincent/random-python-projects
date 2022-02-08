# Last updated 2020.12.09

import string
from random import choice

password = []

print('Simple password generator')
print('This will generate you some randome characters for your password needs\n')
print('Available options:')
print('1. Generate alphanumeric password')
print('2. Generate alphanumeric + punctuation password')
userChoice = int(input('\nPlease enter your selection: '))

if userChoice == 1:
    passChar = string.ascii_letters + string.digits

    passLen = int(input('\nPlease enter the length of the password: '))

    for passLen in range(passLen):
        password.append(choice(passChar))

    print('Your password is: ' + ''.join(password) + '\n')
elif userChoice == 2:
    passChar = string.ascii_letters + string.digits + string.punctuation

    passLen = int(input('\nPlease enter the length of the password: '))

    for passLen in range(passLen):
        password.append(choice(passChar))

    print('Your password is: ' + ''.join(password) + '\n')
else:
    print("Invalid choice. Please try again!")
