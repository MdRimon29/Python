#A function is a set of code which only run when it is called

import random
def get_choices():
    player_choice = input("Enter a choice (rock,paper,scissors): ")
    options=["rock","paper","scissors"] #list
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice} #dictionaries

    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"

    elif player =="rock":
        if computer=="paper":
            return "Paper covers Rock! You lose"
        else:
            return "Rock smashes Scissors! You win"
        
    elif player=="paper":
        if computer=="rock":
            return "Paper covers Rock! You win"
        else:
            return "Scissors cuts Paper! You loss"
            
    elif player=="scissors":
        if computer=="rock":
            return "Rock smashes Scissors! You loss"
        else:
            return "Scissors cuts paper! You win"

choices=get_choices()
result=check_win(choices["player"],choices["computer"])

print(result)
