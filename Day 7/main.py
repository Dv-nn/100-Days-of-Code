import random
from hangman_word import word_list
from hangman_art import stages



def get_guess():
    while True:
        g = input("Guess a letter: ").lower()
        # repeated guesses of the same letter should not count as a "bad" guess
        if g in guessed_letter_list:
            print(f"You have already guessed the letter \"{g}\".")

        elif g not in letter_list:
            print("The guess has to be a single letter. Please try again.")
        else:
            return g


letter_list = list("abcdefghijklmnopqrstuvwxyz")

guessed_letter_list = []


chosen_word = list(random.choice(word_list))
# the display list, fill it with "_" for each character
display = []
for i in range(len(chosen_word)):
    display.append("_")

# set conditions to break out of main loop
game_over = False
is_winner = False

lives = len(stages) - 1

print(f"Pssst, the solution is \"{''.join(chosen_word)}\".")

while not game_over:
    guess = get_guess()

    guessed_letter_list.append(guess)

    # evaluate the guess, and update the display list if needed
    good_guess = False
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
            good_guess = True

    if good_guess:
        # check for win condition
        # count the "_" in the display list, none means all characters have been guessed already
        if display.count("_") == 0:
            is_winner = True
            game_over = True
    else:
        print(f"The letter \"{guess}\" is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True

    print(" ".join(display))
    print(stages[lives])


if is_winner:
    print("You win!")
else:
    print("Game over.")
