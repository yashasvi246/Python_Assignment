def char(a):
    if a=='S':
        return [[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,1],[0,0,0,0,1],[1,1,1,1,1]]
    elif a=='O':
        return [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    elif a=='N':
        return [[1,0,0,0,1],[1,1,0,0,1],[1,0,1,0,1],[1,0,0,1,1],[1,0,0,0,1]]
    elif a=='I':
        return [[1,1,1,1,1],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[1,1,1,1,1]]
    elif a=='Y':
        return [[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0]]
    elif a=='A':
        return [[0,0,1,0,0],[0,1,0,1,0],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]]
    elif a==' ':
        return [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    elif a=='M':
        return [[1,0,0,0,1],[1,1,0,1,1],[1,0,1,0,1],[1,0,0,0,1],[1,0,0,0,1]]
    elif a=='D':
        return [[1,1,1,0,0],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[1,1,1,0,0]]
    elif a=='E':
        return [[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,1],[1,0,0,0,0],[1,1,1,1,1]]
    elif a=='V':
        return [[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0]]
    elif a=='H':
        return [[1,0,0,0,1],[1,0,0,0,1],[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1]]
l=input('Enter in capitals')
s=len(l)
a=[]
b=[]
c=[]
d=[]
e=[]
for k in l:
    n=char(k)
    a.append(n[0])
    b.append(n[1])
    c.append(n[2])
    d.append(n[3])
    e.append(n[4])
f=[a,b,c,d,e]

for i in range(5):
    for k in range(s):
        for j in f[i][k]:
            
            if j==1:
                print("*",end='')
            else:
                print(' ',end='')
        print(' ',end=' ')
    print()
        
   
