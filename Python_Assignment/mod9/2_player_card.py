import random
class Card:
    def __init__(self,face,suit,value):
        self.face=face
        self.suit=suit
        self.value=value

    def __str__():
        return face,suit,value
        
        
class Deck:
    
    def __init__(self,face,suit,value):
        cards=[]
        
        pass
    def add_card(self,c):
        self.c=c
        return cards.append([c.__str__()])
    def shuffle(self):
        return random.shuffle(cards)
    def next_card(self):
        self.nextc=random.choice(cards)
        
        return self.nextc
    def return_card(self):
        cards.remove(self.nextc)
        return cards
        
        
class Hand():
    def __init__(self):
        hand=[]
        pass
        
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
            
                  
                  
                  
            hand=h.draw_from(self.d)
            print(hand)
            self.sum=self.sum+hand[-1][2]
            print('Your Sum is ',self.sum)
            
                  
                              
            return self.credit,self.sum
                              
                        
                              
            print(hand)

class Game:
      def __init__(self,player1,player2):
            self.player1=player1
            self.player2=player2
            self.chance=0
      def play(self,h,d,p):
            self.h=h
            self.d=d
            self.p=p
            u=0
            while(u<20):
                  if self.chance%2==0:
                        print(self.player1,' ,Your Chance .\n')
                        self.credit1,self.sum1=p.play(h,d)
                        if self.sum1>=21:
                              print(self.player1 ,' Wins')
                              print('score :',self.sum1)
                              print(self.player2 ,' Lose')
                              print('score :',self.sum2)
                              break
                              
                        self.chance+=1
                  else:
                        print(self.player2,' ,Your Chance .\n')
                        self.credit2,self.sum2=p.play(h,d)
                        self.chance+=1
                        if self.sum2>=21:
                              print(self.player2 ,' Wins')
                              print('score :',self.sum2)
                              print(self.player1 ,' Lose')
                              print('score :',self.sum1)
                              break
                              
                  
                        
                  u+=1    
                  
            if u>20:
                  win=max(self.sum1,self.sum2)
                  if win==self.sum1:
                        print(player1 ,' Wins')
                        print('score :',self.sum1)
                  if win==self.sum2:
                          print(player2 ,' Wins')
                          print('score :',self.sum2)
                  


                        
                        
def main():
    c=0
    faces={1:'ace',11:'jack',12:'queen',13:'king'}
    suit=['spade','diamond','heart','club']
    for l in range(4):
        for i in range(1,14):
            if i >10 or i==1:
                d=Deck(faces[i],suit[c],i)
                d.add_card()
            else:
                d=Deck(0,suit[c],i)
                d.add_card()
        c+=1
    o=Card()
    h=Hand(cards)
    
    p=Player(hand,'y')
    g=Game(input('Enter the name of the player1'),input('Enter the name of the player2'))
    g.play(h,d,p)
   
    
main()
