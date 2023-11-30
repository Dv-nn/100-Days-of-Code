from data import data
import random
from replit import clear


def format_data(account):
  """Format the account data into printable format"""
  account_name = account_a["name"]
  account_descr = account_a["description"]
  account_country = account_a["country"]
  print(f"{account_name}, {account_descr} from {account_country}")

def check_answer(guess, a_followers, b_followers):
  """Check if user is correct using IF statement"""
    if a_followers > b_followers:
        return guess == "a" 
    else:
        return guess == "b"  

score = 0
game_should_continue = True
account_a = random.choice(data)
# Make the game repeatable
while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")
  
# Ask user for a guess
 guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Chect if user is correct
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
is_correct = check_answer(guess, a_follower_count, b_follower_count)

# Clear the screen between rounds
clear()

# Use if statement to check if user is correct

# Give user feedback on their guess

# Score keeping
if is_correct:
        score += 1
        print(f"You're Right! Current Score: {score}\n")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final Score: {score}\n")
       
        

