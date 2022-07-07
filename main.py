import random
import time

def deck_generator(num_of_cards):

    deck_count = [  'Ace of ', 'One of ', 'Two of ', 'Three of ', 'Four of ',
                    'Five of ', 'Six of ', 'Seven of ', 'Eight of ', 'Nine of ',
                    'Ten of ', 'Jack of ', 'King of ', 'Queen of ']

    deck_suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    new_deck = []

    i = 0
    while i < num_of_cards:
        count = deck_count[random.randint(0, len(deck_count)-1)]
        suit = deck_suit[random.randint(0, len(deck_suit)-1)]
        new_card = count + suit
        if new_card not in new_deck:
            new_deck.append(new_card)
            i += 1
        else: print("We had a duplicate, readjusting...")
    return new_deck


def guesser(deck):
    stack1 = 

print("I'm going to read your mind........")
time.sleep(2)
print("Press G to generate a brand new deck of 21 cards: ")
input()
print("generating..............")
time.sleep(3)
deck = deck_generator(21)

print("Here is your deck...")

i = 0

while i < len(deck):
    print(f"{deck[i]}     {deck[i+1]}       {deck[i+2]}")
    i += 3

print("""
        Pick a card, any card and memorize!!
        When you're ready, press R and I will read your mind ;)""")
input()

guesser(deck)