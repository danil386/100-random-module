import random

def rand100():
    x = random.randint(1,100)
    y = 0
    z = 0
    while y != x:
        y = input("Enter a number: ")
        y = float(y)
        if y != x:
            print("Not quite. Try again")
        if y > x:
            print("Your guess was too high")
        elif y < x:
            print("Your guess was too low")
        z = z +1
    if y == x:
        print(f"Congratulations! You guessed the number in {z} guesses!")


if __name__ == "__main__":
    rand100()