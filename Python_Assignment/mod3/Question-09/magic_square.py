# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 23:43:41 2019

@author: windows 8.1
"""
def magic_square(n):
    magicSquare=[]
    for i in range(n):
       l=[]
       for j in range(n):
           l.append(0)
       magicSquare.append(l)
    i=n//2
    j=n-1
    count=1
    num=n*n
    while(count<=num):
        
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(i==-1):
                i=n-1
            if(j==n):
                j=0
        if(magicSquare[i][j]!=0):
                j=j-2
                i=i+1
                continue;
        else:
            magicSquare[i][j]=count
            count=count+1
        i=i-1
        j=j+1
    
   
    
    #display
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=' ')
        print()
    print('Sum of the magic Square of order',n,' is : ',sum(magicSquare[0]))
order=input("enter the order of the matrix: ") 
order=int(order)
magic_square(order)
