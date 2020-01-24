n=int(input('Enter a Pocket Number from 0 to 36'))
if(n>36):
    print("Error !!! ..Please Enter Pocket Number Ranging from 0 to 36")
else:
    if(n==0):
        print('Pocket is green')
    elif(n>=1 and n<=10):
        if(n%2==0):
            print('Pocket is  Black')
        else:
            print('Pocket is Red')
    elif(n>=11 and n<=18):
        if(n%2==0):
            print('Pocket is  Red')
        else:
            print('Pocket is Black')
    elif(n>=19 and n<=28):
        if(n%2==0):
            print('Pocket is  Black')
        else:
            print('Pocket is Red')
    elif(n>=29 and n<=36):
        if(n%2==0):
             print('Pocket is  Red')
        else:
            print('Pocket is Black')
    
