from random import randint


class Card:
    CARD_TYPE = ["Clubs", "Spades", "Diamonds", "Hearts"]
    CARD_VALUE = ["Ace", "King", "Queen", "Jack",
                  "10", "9", "8", "7", "6", "5", "4", "3", "2"]

    def __init__(self, types, values):
        self.type = types
        self.value = values

    def __repr__(self):
        return self.CARD_VALUE[self.value] + " of " + self.CARD_TYPE[self.type]


def perfectly_random(k):
    return randint(1, k)


def shuffle_cards_by_swapping(cards):
    array_len = len(cards)-1
    for index in range(0, array_len):
        ran = perfectly_random(array_len)
        temp = cards[index]
        cards[index] = cards[ran]
        cards[ran] = temp
    return cards


cards = [Card(a, b) for a in range(0, 4) for b in range(0, 13)]
print("Before: {}".format(cards))
print("<>" * 70)
cards_random = shuffle_cards_by_swapping(cards.copy())
print("After: {}".format(cards_random))

dif = 0
for i in range(0, len(cards)):
    if (cards[i] is not cards_random[i]):
        dif += 1
print("<>" * 70)
print("{} Cards are on the same position.".format(len(cards)-dif))
