import random
class Card:
    def __init__(self,face,suit,value):
        self.face=face
        self.suit=suit
        self.value=value
    
    def __str__(self):
        return self.face,self.suit,self.value
        
        
class Deck:
    def __init__(self,cards):
        
        self.cards=cards
        
        
        
    def add_card(self,face,suit,value,cards,o):
        self.o=o
        o.__init__(face,suit,value)
        return self.cards.append(o.__str__()) 
    def shuffle(self):
        return random.shuffle(self.cards)
    def next_card(self):
        self.nextc=random.choice(self.cards)
        
        return self.nextc
    def return_card(self):
        self.cards.remove(self.nextc)
        return self.cards
        
        
class Hand():
    def __init__(self):
        self.hand=[]
    def draw_from(self,d):
        self.d=d
        
        self.card_drawn=self.d.next_card()
        print('Card you have Choosen is :',self.card_drawn)
        self.card=self.d.return_card()
        self.hand.append(self.card_drawn)
        ch=int(input('Enter 1 to return the card.\nEnter 0 to not return card.\n'))
        if ch==1:
            self.return_to()
        
            
        return self.hand
    def return_to(self):
        
        return self.hand.append(self.card_drawn)

class Player:
      def __init__(self,name,h):
            self.credit=0
            self.name=name
            self.sum=0
            
      def play(self,h,d):
            self.h=h
            self.d=d
            while True:
                  self.d=d
                  self.d.shuffle()
                  hand=h.draw_from(self.d)
                  print(hand)
                  self.sum=self.sum+hand[-1][2]
                  print('Your Sum is ',self.sum)
                  if self.sum>=21:
                        print('Hurray!! ,You Win')
                        ch=int(input('Enter 1 to Play again.\nEnter 0 to Quit.\n'))
                        print('You had choosen ',h.hand)

                        h.hand.clear()
                        self.sum=0
                        
                        if ch==0:
                              print('credit of ',self.name,' is ',self.credit)
                              break
                        else:
                            print('Invalid Input')
                    
                            
def main():
    c=0
    o=Card('0','0',0)
            
    cards=[]
    faces={1:'ace',11:'jack',12:'queen',13:'king'}
    suit=['spade','diamond','heart','club']
    for l in range(4):
        for i in range(1,14):
            if i >10 or i==1:
                d=Deck(cards)
                d.add_card(faces[i],suit[c],i,cards,o)
            else:
                d=Deck(cards)
                d.add_card(0,suit[c],i,cards,o)
        c+=1
    
    h=Hand()
    
    p=Player('yashasvi',h)
    p.play(h,d)
    
main()
