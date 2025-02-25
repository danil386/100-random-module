import random

def title():
    print("Rock, Paper, Scissors")
    print("Instructions: When prompted, enter either rock, paper, or scissors. \nRock beats scissors, paper beats rock, and scissors beats paper. \nThe goal of the game is to beat the computer, who will make a random choice between the three every time.")

def game():
    options = ["rock", "paper", "scissors"]
    pchoice = input("Enter rock, paper or scissors: ")
    cchoice = random.choice(options)
    print(f"The computer chose {cchoice}")
    list = [pchoice,cchoice]
    if pchoice in options:
        if (pchoice == "scissors" and cchoice == "rock") or (pchoice == "rock" and cchoice == "paper") or (pchoice == "paper" and cchoice == "scissors"):
            print("You Lost")
        elif pchoice == cchoice:
            print("Draw")
        else:
            print("You win")
    else:
        print("The value you entered is not valid")


title()
game()