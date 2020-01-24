class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str__(self):
        return [f'a {self.color} car',f'mileage {self.mileage}']
        
a=Car('red',12)
print(a.__str__()[0])
print(a.__str__()[1])

    
