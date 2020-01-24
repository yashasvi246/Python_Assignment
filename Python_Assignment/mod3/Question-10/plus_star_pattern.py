n=int(input('Enter any Number'))
for i in range(2*n+1):
    for j in range(2*n+1):
        if(j==n):
            print('*',end=' ')

        elif(i==n and j!=n):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
