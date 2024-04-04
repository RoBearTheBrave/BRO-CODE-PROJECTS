#create a rock, paper, scissors game

import random

#since we don't want these options to change a tuple is better than a list
options = ("rock", "paper", "scissors")
game_running = True


while game_running:

    player_choice = None
    computer_choice = random.choice(options)

    while player_choice not in options:
        player_choice = input("Enter rock, paper, or scissors: ").strip().lower()

    print(f"Player: {player_choice}")
    print(f"Computer: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("Player wins!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Player wins!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")

    if input("Enter 'yes' to play again: ").strip().lower() != "yes":
        game_running = False
        print("Thanks for playing!")