import random


playerloss = ["scissors", "rock"] , ["paper", "scissors"] , ["rock", "paper"] , ["lizard", "rock"] , ["spock", "lizard"] , ["scissors", "spock"] , ["lizard", "scissors"] , ["spock", "paper"] , ["rock","spock"] , ["paper","lizard"]


def title():
    print("Rock, Paper, Scissors, Lizard, Spock")
    print("Instructions: When prompted, enter either rock, paper, scissors, lizard, or spock. \nScissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock, and as it always has, Rock crushes Scissors. \nThe goal of the game is to beat the computer, who will make a random choice between the five every time.")

def game():
    options = ["rock", "paper", "scissors", "lizard", "spock"]
    pchoice = input("\nEnter rock, paper, scissors, lizard, or spock: ")
    cchoice = random.choice(options)
    print(f"The computer chose {cchoice}")
    list = [pchoice,cchoice]
    a,b,c,d,e,f,g,h,i,j = playerloss
    losses = [a,b,c,d,e,f,g,h,i,j]
    if pchoice in options:
        if list in losses:
            print("You Lost")
        elif pchoice == cchoice:
            print("Draw")
        elif list!=playerloss:
            print("You win")
    else:
        print("The value you entered is not valid")


title()
game()