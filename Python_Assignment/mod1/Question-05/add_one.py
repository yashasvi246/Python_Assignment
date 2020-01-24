x=int(input('Enter a 5 digit No.'))
x=list(map(int, str(x)))
z=''
for i in x:
    y=i+1
    z=z+str(y)
print(z)
