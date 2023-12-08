file = open("my_file.txt")
contents = file.rad()
print(contest)
file.close()

# ____________________________
with open("my_file.txt") as file:
  contents = file.read()
  print(contest)

# ____________________________
with open("my_file.txt", mode="w") as file:
  file.write("\nNew text")


#______________________________
PLACEHOLDER =["name"]

with open("...txt") as names_file:
  names = names_file.readlines()

with open(...txt) as letter_file:
  letter_contents = letter_file.read()
  for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
    with open(f"..{stripped_name}.txt", mode="w") as completed_letter:
      completed_letter.write(new_letter)
    
