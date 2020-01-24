x=int(input('Enter a 5 digit No.'))
sum=0
for i in range(5):
    y=x%10
    sum=sum+y
    x=x//10
print(sum)
