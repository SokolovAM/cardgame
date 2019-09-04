# Card game "Drunkard"

class Card:
    
    suits=['spades','hearts','diamands','clubs']
    
    values=[None,None,'2','3',
                '4','5','6','7','8','9','10',
                'Jack','Queen','King','Ace']

    def __init__(self,v,s):
        """suit & values - integers"""
        self.value = v
        self.suit = s

    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
    #Give value and suit of the card
        
        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v


from random import shuffle

 
class Deck:
    #Deck forming

    def __init__(self):
        self.cards=[]
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        #Remove card from deck
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    #Player's status

    def __init__(self,name):
            self.name = name
            self.wins = 0
            self.card = None


class Game:
    
    def __init__(self):
        name1 = input('Input the name of first player: ')
        name2 = input('Input the name of second player: ')
        self.deck=Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "{} taking the card".format(winner)
        return w

    def draw(self, p1n, p2n,p1c, p2c):
        d = "{} putting {}\n{} putting {}".format(p1n,p1c,p2n,p2c)
        print(d)

    def gameplay(self):
        cards=self.deck.cards
        print('Start game!')
        while len(cards) >= 2:
            msg = 'Press X to exit, press any other button to start the game: '
            res = input(msg)
            if res.upper() == 'X':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p2n,p1c, p2c)
            if p1c > p2c:
                self.p1.wins +=1
                self.wins(p1n)
            else:
                self.p2.wins +=1
                self.wins(p2n)

        win = self.winner(self.p1, self.p2)

        print('-'*50)
        print('{} wins: {}'.format(p1n,self.p1.wins))
        print('{} wins: {}'.format(p2n,self.p2.wins))
        print("Game over! {}".format(win))
        

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name + ' is winner!'
        if p1.wins < p2.wins:
            return p2.name + ' is winner!'
        return "Draw!"
            
game = Game()
game.gameplay()

                

    
    
        
