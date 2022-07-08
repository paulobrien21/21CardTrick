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


def split_deck(deck):

    stack1 = []
    stack2 = []
    stack3 = []

    i = 0

    while i < 21:
        if len(stack1) == len(stack3):
            stack1.append(deck.pop(0))
        elif len(stack2) == len(stack3):
            stack2.append(deck.pop(0))
        else:
            stack3.append(deck.pop(0))
        i += 1
    return stack1, stack2, stack3



def reassemble_deck(stack1, stack2, stack3, select):

    deck = []

    if select == '1':
        stack2.extend(stack1)
        stack2.extend(stack3)
        deck = stack2[:]
        print(f"newly assembled deck: {deck}")
    elif select == '2':
        stack1.extend(stack2)
        stack1.extend(stack3)
        deck = stack1[:]
        print(f"newly assembled deck: {deck}")
    else:
        stack1.extend(stack3)
        stack1.extend(stack2)
        deck = stack1[:]
        print(f"newly assembled deck: {deck}")

    return deck


def guesser(deck):

    for i in range(3):
        stack1, stack2, stack3 = split_deck(deck)
        print(f"group 1: {stack1}")
        print(f"group 2: {stack2}")
        print(f"group 3: {stack3}")

        print("which group is your card in?")
        select = input()
        deck = reassemble_deck(stack1, stack2, stack3, select)

    correct_card = deck[10]

    return correct_card

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

correct_card = guesser(deck)

print(f"Your card was........The {correct_card}! ;)")
