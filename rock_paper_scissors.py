# We will write a rock paper scissors game in class - Complete it in this file
import random
player_choice = "rock"
computer_choice = "paper"

#create a function that gets the choices
def get_choices():
    options = ["rock", "paper","scissors"]
    player_choice = input("Enter a choice.  rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

#function to check for a win
def check_win(player, computer):
    print("you chose {player}, computer chose {computer}")
    if player == computer:
        return "it's a tie" 
    elif player == "rock":
        if compuer == "scissors":
            return "rock smashes scissors, you win"
        else:
            return "paper smashes rock"
result = check_win(choices["player"], choices["computer"])
print (result)
#choices = get_choices()
#print(choices)