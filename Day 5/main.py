# Password Generator

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

print("How many letters would you like in your password?")
nr_letters = int(input("> "))
print("How many symbols would you like?")
nr_symbols = int(input("> "))
print("How many numbers would you like?")
nr_numbers = int(input("> "))

# Easy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# change this to False for "Easy Level"
hard_level = True

blueprint = []

if nr_letters > 0:
    for i in range(nr_letters):
        blueprint.append("l")

if nr_symbols > 0:
    for i in range(nr_symbols):
        blueprint.append("s")

if nr_numbers > 0:
    for i in range(nr_numbers):
        blueprint.append("n")

# the blueprint list should look something like this now: ["l", "l", "l", "s", "s", "n", "n"]
# for "Hard Level", shuffle the placeholder elements in the blueprint
# for "Easy Level", leave as is
if hard_level:
    # this works (as in, no error) even if the length of the list is 0, so skipping the check
    random.shuffle(blueprint)

password = ""
for placeholder in blueprint:
    if placeholder == "l":
        password += random.choice(letters)
    elif placeholder == "s":
        password += random.choice(symbols)
    elif placeholder == "n":
        password += random.choice(numbers)

# print the result, unless the inputs were all "0"
if len(password) > 0:
    print(f"Here is your password: {password}")
else:
    print("You need to choose at least 1 character to generate a password.")
