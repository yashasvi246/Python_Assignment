import random
class Coin:
    def __init__(self):
        self.sideup='Head'
    def toss(self):
        if random.randint(0,1)==0:
            self.sideup='Head'
        else:
            self.sideup='Tail'
    def get_sideup(self):
        return self.sideup
def main():
    a=Coin()
    print('This Side Up :',a.get_sideup())
    print('I am Tossing the coin')
    a.toss()
    print('This side up :',a.get_sideup())

main()
