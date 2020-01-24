n,m=map(int,input().split(' '))
ma=0
e=list(map(int,input('Enter the fruit value').split(' ')))
for i in range(n):
    if(i+m>n-1):
        s=sum(e[i:])+sum(e[0:i+m-n])
    else:
        s=sum(e[i:i+m])
    if(s>ma):
        ma=s
        continue
    
print(ma)
