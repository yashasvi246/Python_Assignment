import random
class Card:
    def __init__(self,face,suit,value):
        self.face=face
        self.suit=suit
        self.value=value
    def add_card(self):
        return cards.append([self.face,self.suit,self.value])
    def __str__():
        return face,suit,value
        
        
class Deck:
    def __init__(self,cards):
        self.cards=cards
        pass 
    def shuffle(self):
        return random.shuffle(cards)
    def next_card(self):
        self.nextc=random.choice(cards)
        
        return self.nextc
    def return_card(self):
        cards.remove(self.nextc)
        return cards
        
        
class Hand():
    def __init__(self,cards):
        self.cards=cards
        
    def draw_from(self,d):
        self.d=d
        self.d.shuffle()
        self.card_drawn=self.d.next_card()
        print('Card you have Choosen is :',self.card_drawn)
        self.card=self.d.return_card()
        hand.append(self.card_drawn)
        ch=int(input('Enter 1 to return the card.\nEnter 0 to not return card.\n'))
        if ch==1:
            self.return_to(d)
        
            
        return hand
    def return_to(self,d):
        self.d=d
        return self.card.append(self.card_drawn)

class Player:
      def __init__(self,name,hand):
            self.credit=0
            self.name=name
            self.hand=hand
            self.sum=0
      def play(self,h,d):
            self.h=h
            self.d=d
            while True:
                  
                  
                  
                  hand=h.draw_from(self.d)
                  
                  self.sum=self.sum+hand[-1][2]
                  print('Your Sum is ',self.sum)
                  if self.sum>=21:
                        print('Hurray!! ,You Win')
                        ch=int(input('Enter 1 to Play again.\nEnter 0 to Quit.\n'))
                        if ch==0:
                              print('credit of ',self.name,' is ',self.credit)
                        break
            print(hand)

                              
def main():
    c=0
    for l in range(4):
        for i in range(1,14):
            if i >10 or i==1:
                o=Card(faces[i],suit[c],i)
                o.add_card()
            else:
                o=Card(0,suit[c],i)
                o.add_card()
        c+=1
    d=Deck(cards)
    h=Hand(cards)
    
    p=Player('y',hand)
    p.play(h,d)
    
    
    
    
                    
        

faces={1:'ace',11:'jack',12:'queen',13:'king'}
suit=['spade','diamond','heart','club']
cards=[]
hand=[]    
    
main()
