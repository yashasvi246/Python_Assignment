Quantity=int(input('Enter the Number of Packages: '))
discount=0
amount =99*Quantity
if(Quantity>=10 and Quantity<20 ):
    discount=amount*0.1
elif(Quantity>=20 and Quantity<50):
    discount=amount*0.2
elif(Quantity>=50 and Quantity<100):
    discount=amount*0.3
elif(Quantity>=100):
    discount=amount*0.4
amount=amount-discount
if(discount>0):
    print('Your Discount is : $',discount)
    print('Your Total amount after the discount is : $',amount)
else:
    print('Your Total amount is : $',amount)
    
