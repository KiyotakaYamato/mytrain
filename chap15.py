# chapter15 card game 'War'

from random import shuffle


class Card :
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s) :
        """マーク（スート）も値も整数値です"""
        self.value = v
        self.suit = s

    def __lt__(self, c2) :
        if self.value < c2.value :
            return True
        if self.value == c2.value :
            if self.suit < c2.suit :
                return True
            else :
                return False
        return False

    def __gt__(self, c2) :
        if self.value > c2.value :
            return True
        if self.value == c2.value :
            if self.suit > c2.suit :
                return True
            else :
                return False
        return False

    def __repr__(self) :
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck :
    def __init__(self) :
        self.cards = []
        for i in range(2, 15) :
            for j in range(4) :
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self) :
        if len(self.cards) == 0 :
            return
        return self.cards.pop()

class Player :
    def __init__(self, name) :
        self.wins = 0
        self.card = None
        self.name = name

class Game :
    def __init__(self) :
        name1 = input("Player1's name : ")
        name2 = input("Player2's name : ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner) :
        wmsg = "このラウンドは {} が勝ち"
        wmsg = wmsg.format(winner)
        print(wmsg)

    def draw(self, p1na, p1cd, p2na, p2cd) :
        dmsg = "{}は{}、{}は{}を引きました"
        dmsg = dmsg.format(p1na, p1cd, p2na, p2cd)
        print(dmsg)

    def play_game(self) :
        cards = self.deck.cards
        print("Start game Now!")
        while len(cards) >= 2 :
            gmsg = "qで終了、その他は継続:"
            res = input(gmsg)
            if res == "q" :
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c :
                self.p1.wins += 1
                self.wins(self.p1.name)
            else :
                self.p2.wins += 1
                self.wins(self.p2.name)

        winp =self.winner(self.p1, self.p2)
        print("End Game, {} wins! Conglat!".format(winp))

    def winner(self, p1, p2) :
        if p1.wins > p2.wins :
            return p1.name
        if p1.wins < p2.wins :
            return p2.name
        return "Draw game..."

mygame = Game()
mygame.play_game()
