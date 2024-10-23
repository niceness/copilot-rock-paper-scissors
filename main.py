#!/usr/bin/python3
# Write a Roshambo game
# TODO: extend to include Lizard and Spock?

import random

# define main function
def main():
    # define the game choices
    choices = ["rock", "paper", "scissors", "lizard", "spock"]

    # get the user's choice
    user_choice = input("Choose rock, paper, scissors, lizard, or spock: ")

    # get the computer's choice
    computer_choice = random.choice(choices)

    # print the choices
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    # determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
         (user_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (user_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (user_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (user_choice == "spock" and (computer_choice == "scissors" or computer_choice == "rock")):
        print("You win!")
    else:
        print("Computer wins!")

# call the main function
if __name__ == "__main__":
    main()
exit