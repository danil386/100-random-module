import random

def roll():
    x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    x3 = random.randint(1,6)
    stat = x1 + x2 + x3
    print(f"You got {stat}")

    return stat

def dnd():
    print("Welcome to a Dungeons and Dragons character generator!")
    input("To determine your strength press enter: ")
    strength = roll()
    input("To determine your intelligence press enter: ")
    intelligence = roll()
    input("To determine your wisdom press enter: ")
    wisdom = roll()    
    input("To determine your dexterity press enter: ")
    dexterity = roll() 
    input("To determine your constitution press enter: ")
    constitution = roll()       
    input("To determine your charisma press enter: ")
    charisma = roll()
    print(f"\n\nYour character has:\na strength of {strength}\nan intelligence of {intelligence}\na wisdom of {wisdom}\na dexterity of {dexterity}\na constitution of {constitution}\na charisma of {charisma}")


dnd()