# Create a number guessing game.
# The program should pick a random number between 1 and 100 and the user has to guess it.
# The program should provide "Too high" or "Too low" hints.
# Use a while loop that terminates when the user guesses correctly.

import random

secret_number = random.randint(1, 100)
user_guess = 0

while user_guess != secret_number:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess < 1 or user_guess > 100:
        print("Please guess a number within the range of 1 to 100.")
    elif user_guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

print("Congratulations! You've guessed the correct number:", secret_number)
