import random

deck = ["ace of clubs","2 of clubs","3 of clubs","4 of clubs","5 of clubs","6 of clubs","7 of clubs","8 of clubs","9 of clubs","10 of clubs","jack of clubs","queen of clubs","king of clubs","ace of spades","2 of spades","3 of spades","4 of spades","5 of spades","6 of spades","7 of spades","8 of spades","9 of spades","10 of spades","jack of spades","queen of spades","king of spades","ace of hearts","2 of hearts","3 of hearts","4 of hearts","5 of hearts", "6 of hearts","7 of hearts","8 of hearts","9 of hearts","10 of hearts","jack of hearts","queen of hearts","king of hearts","ace of diamonds","2 of diamonds","3 of diamonds","4 of diamonds","5 of diamonds","6 of diamonds","7 of diamonds","8 of diamonds","9 of diamonds","10 of diamonds","jack of diamonds","queen of diamonds","king of diamonds"]

def shuffle():
    random.shuffle(deck)

    return deck


def deal(deck):
    hand1 = []
    for x in range(0,5):
        x = random.choice(deck)
        hand1.append(x)
        deck.remove(x)
    hand2=[]
    for x in range(0,5):
        x = random.choice(deck)
        hand2.append(x)
        deck.remove(x)
    return hand1, hand2   


def main():
    print("Welcome players! You will each now be dealt 5 cards")
    g = shuffle()
    hands = deal(g)
    print(f"Player 1, you received {hands[0]}")
    print(f"Player 2, you received {hands[1]}")

main()