"""
扑克游戏
"""
import random

from enum import Enum


# class Direction(Enum):
#     UP, RIGHT, DOWN, LEFT = range(4)
#
# class Gender(Enum):
#     MALE, FEMALE, UNKNOWN = range(1, 4)

class Suite(Enum):
    """花色（枚举）"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """牌（一张牌）"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __lt__(self, other):
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

    def __repr__(self):
        suites = ['♠', '♥', '♣', '♦']
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'


# for suite in Suite:
#     print(suite, suite.value)
#
# card1 = Card(Suite.CLUB,5)
# card2 = Card(Suite.HEART,12)
# print(card1, card2)

class Poker:
    """扑克（一副牌）"""

    def __init__(self):
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.index = 0

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards[self.index]
        self.index += 1
        return card

    @property
    def has_more(self):
        return self.index < len(self.cards)


# poker = Poker()
# poker.shuffle()
# print(poker.cards)


class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


def main():
    poker = Poker()
    poker.shuffle()
    players = [Player('东'), Player('西'), Player('南'), Player('北')]
    for _ in range(3):
        for player in players:
            if poker.has_more:
                card = poker.deal()
                player.get_one(card)
    for player in players:
        player.arrange()
        print(f'{player.name}:', end='')
        print(player.cards)


if __name__ == '__main__':
    main()
