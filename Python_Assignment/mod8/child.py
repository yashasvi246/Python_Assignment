from Automobile import Automobile 
class Car(Automobile):
    def __init__(self,__make,__model,__mileage,__price,__doors):
        Automobile.__init__(self,__make,__model,__mileage,__price)
        self.__doors=__doors
    def set_doors(self,__doors):
        self.__doors=__doors
    def get_doors(self):
        return self.__doors
    '''def __str__(self):
        return 
    '''
def main():
    a=Car('Hyundai',8,75,600000,4)
    print(f'a car which make by {a.get_make()} and model is {a.get_model()} whose mileage and price is {a.get_mileage()},{a.get_price()}.The Car has {a.get_doors()} doors')
    print('NOW I AM SETTING NEW VALUE OF MODEL AS 3')
    a.set_model(3)
    
    print(a.get_doors())
main()
