import random

def headstails():
    guess = input("Heads or Tails? ")
    x = random.randint(1,2)
    if x == 1:
        y = "Heads"
        y = str(y)
    elif x == 2:
        y = "Tails"
        y = str(y)
    if guess == y:
        print(f"You were correct! It was {y}")
    else:
        print(f"You were incorrect. It was {y}")

if __name__ == "__main__":
    headstails()