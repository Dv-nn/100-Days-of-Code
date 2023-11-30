from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
  """
  Function to check user's guess against actual answer
  """
  if guess > answer:
    print("To high.")
    return turns - 1
  elif guess < answer:
    print("To low.")
    return turns - 1
  else:
    print(f"You go it! The answer was {answer}.")


def set_difficulty():
  """
  Make function to set diffuculty
  """
  level = input("Choose a difficulty. Type easy or hard: ")
  if level == "easy":
    turns = EASY_LEVEL_TURNS
  else:
    turns = HARD_LEVEL_TURNS

def game:
  # Choosing  a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm Thinking of a number between 1 a 100.")
  answer = randint(1, 100)
  print(f"Psssst, the correct answer is {answer}.")
  
  turns = set_difficulty()
  # Repeat the guessing functionality if they get it wrong
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    
    # Let the user guess a number
    guess = int(input("Make a guess: "))
    # Track the number of turns and reduce by 1 if they get it wrong
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
