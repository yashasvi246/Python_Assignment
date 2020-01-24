n=int(input('Enter any Positive integer'))


p=n//2
l=-1
for i in range(n):
    if(i==0):
        print(' '*p,'*',end='\n')
        
    elif(i==n-1):
        print('* '*n,end='')
    else:
                #print(p)
        print(' '*p,'*',' '*l,'*',end='\n')
        l=l+2
        p=p-1


