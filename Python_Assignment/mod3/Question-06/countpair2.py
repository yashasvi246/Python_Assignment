def count_pair(a,b,x):
    c=0
    for i in range(len(a)):
        if(x-a[i])in b:
            c=c+b.count(x-a[i])
    return c
    
a=list(map(int,input('Enter list1')))
b=list(map(int,input('Enter list2')))
x=int(input('Enter sum'))

print(count_pair(a,b,x))
