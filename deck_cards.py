import random as rd


class Deck:

    def __init__(self, cards):
        self.cards = cards

    def shuffle(self):
        rd.shuffle(self.cards)


    def deal(self):

        return self.cards.pop()

    def count_remaining(self):
        pass


class Card:
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def present(self):
        print(f" {self.value} of {self.suit}")


card_list = []

for suit in Card.suits:
    for value in Card.values:
        card_list.append(Card(suit,value))
        print(f"card added in the list  {value} of {suit}")

deck = Deck(card_list)
deck.shuffle()
deal = deck.deal()
deal.present()
