# Guess the Number Game

import random

computer_number = random.randint(1, 100)
user_guess = input("Guess a number a between 1 and 100: ")
attempts = 0
running = True

while running:
    if not user_guess.isdigit():
        user_guess = input("Please enter a valid number: ")
        continue

    user_guess = int(user_guess)
    attempts += 1

    if user_guess < computer_number:
        user_guess = input('Too low! Try again: ')
        print()
    elif user_guess > computer_number:
        user_guess = input('Too high! Try again: ')
        print()
    else:
        print(
            f"Congratulations! You have guessed a right Number {computer_number} in attempts {attempts}.")
        running = False
