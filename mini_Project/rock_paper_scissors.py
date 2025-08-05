# Rock, Paper, Scissors Game

import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
user_choice = input("Enter rock, paper, or scissors: ").lower()
running = True

while True:
    if (user_choice not in options):
        user_choice = input(
            "Invalid choice! Please enter rock, paper, or scissors: ").lower()
        continue
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print(f"It's a tie! You both chose {user_choice}.")
        is_continue = input("Do you want to play again? (yes/no): ").lower()
        if is_continue == 'yes':
            computer_choice = random.choice(options)
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            continue
        else:
            print("Thanks for playing!")
            break
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You win! {user_choice} beats {computer_choice}.")
        is_continue = input("Do you want to play again? (yes/no): ").lower()
        if is_continue == 'yes':
            computer_choice = random.choice(options)
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            continue
        else:
            print("Thanks for playing!")
            break
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")
        is_continue = input("Do you want to play again? (yes/no): ").lower()
        if is_continue == 'yes':
            computer_choice = random.choice(options)
            user_choice = input("Enter rock, paper, or scissors: ").lower()
        else:
            print("Thanks for playing!")
            break
