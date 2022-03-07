"""
1. Write a python script that creates a deck of cards
and returns two randomly chosen ones to the screen.


HINT: see the standard library package "random"
"""

import random 


class Deck:
    
    def __init__(self):
        ranks = [c for c in range(2,11)] + "J Q K A".split()
        # non list-comprehension way
        # r2 = []
        # for crd in range(2, 11):
        #     r2.append(crd)
        # print(ranks)
        # suits
        suits = "spades clubs diamonds hearts".split()
        # make list of cards
        cards = []
        for rank in ranks:
            for suit in suits:
                card = (rank, suit)
                cards.append(card)
        self.cards = cards
        # c2 = [(rank, suit) for rank in ranks for suit in suits]
        
        # print(cards)
        
        #current_deck = cards.copy()
    def shuffle(self):
        random.shuffle(self.cards)
        # print(current_deck.pop(), current_deck.pop())


d1 = Deck()
d2 = Deck()

print(d1.cards)
d1.shuffle()
print("\nd1\n")
print(d1.cards)

print("\nd2\n")
print(d2.cards)
