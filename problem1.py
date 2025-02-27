import random

def rolloriginal():
    x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    x3 = random.randint(1,6)
    stat = x1 + x2 + x3
    print(f"You got {stat}")

    return stat

def original():
    print("You have chosen option 1: Roll 3 dice for each statistic.")
    input("To determine your strength press enter: ")
    strength = rolloriginal()
    input("To determine your intelligence press enter: ")
    intelligence = rolloriginal()
    input("To determine your wisdom press enter: ")
    wisdom = rolloriginal()    
    input("To determine your dexterity press enter: ")
    dexterity = rolloriginal() 
    input("To determine your constitution press enter: ")
    constitution = rolloriginal()       
    input("To determine your charisma press enter: ")
    charisma = rolloriginal()
    print(f"\n\nYour character has:\na strength of {strength}\nan intelligence of {intelligence}\na wisdom of {wisdom}\na dexterity of {dexterity}\na constitution of {constitution}\na charisma of {charisma}")

def fourdiscardroll():
    x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    x3 = random.randint(1,6)
    x4 = random.randint(1,6)
    four = [x1,x2,x3,x4]
    list.sort(four)
    print(four)
    stat = four[3]+four[2]+four[1]
    print(f"You got {stat}")

    return stat

def fourdiscard():
    print("You have chosen option 2: Roll 4 dice and discard the lowest.")
    input("To determine your strength press enter: ")
    strength = fourdiscardroll()
    input("To determine your intelligence press enter: ")
    intelligence = fourdiscardroll()
    input("To determine your wisdom press enter: ")
    wisdom = fourdiscardroll()    
    input("To determine your dexterity press enter: ")
    dexterity = fourdiscardroll() 
    input("To determine your constitution press enter: ")
    constitution = fourdiscardroll()       
    input("To determine your charisma press enter: ")
    charisma = fourdiscardroll()
    print(f"\n\nYour character has:\na strength of {strength}\nan intelligence of {intelligence}\na wisdom of {wisdom}\na dexterity of {dexterity}\na constitution of {constitution}\na charisma of {charisma}")

def rerollroll():
    x1 = random.randint(1,6)
    while x1 == 1:
        x1 = random.randint(1,6)
    x2 = random.randint(1,6)
    while x2 == 1:
        x2 = random.randint(1,6)
    x3 = random.randint(1,6)
    while x3 == 1:
        x3 = random.randint(1,6)
    stat = x1 + x2 + x3
    print(f"You got {stat}")

    return stat

def threereroll():
    print("You have chosen option 3: Roll 3 dice and reroll 1s.")
    input("To determine your strength press enter: ")
    strength = rerollroll()
    input("To determine your intelligence press enter: ")
    intelligence = rerollroll()
    input("To determine your wisdom press enter: ")
    wisdom = rerollroll()    
    input("To determine your dexterity press enter: ")
    dexterity = rerollroll() 
    input("To determine your constitution press enter: ")
    constitution = rerollroll()       
    input("To determine your charisma press enter: ")
    charisma = rerollroll()
    print(f"\n\nYour character has:\na strength of {strength}\nan intelligence of {intelligence}\na wisdom of {wisdom}\na dexterity of {dexterity}\na constitution of {constitution}\na charisma of {charisma}")    

def dnd():
    print("Welcome to a Dungeons and Dragons character generator!")
    print("We have three options you can either: \n1. Roll 3 dice for each statistic\n2. Roll 4 dice and discard the lowest\n3. Roll 3 dice and reroll 1's")
    choice = input("Enter 1, 2 or 3 to select the respective option: ")
    choice = float(choice)
    if choice == 1:
        original()
    elif choice == 2:
        fourdiscard()
    elif choice == 3:
        threereroll()
    else:
        print("Error. You did not select 1, 2 or 3.")



dnd()