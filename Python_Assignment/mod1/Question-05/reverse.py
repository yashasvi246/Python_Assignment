x=int(input('Enter an Number'))
rev=0
while x!=0:
        y=x%10
        rev=rev*10+y
        x=x//10

print('Reverse of a Number is',rev)
