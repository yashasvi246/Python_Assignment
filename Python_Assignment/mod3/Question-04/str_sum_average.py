s=input('Enter marks').split(' ')

b=[int(s[i]) for i in range(2,len(s),3)]
print('sum',sum(b),'percentage',round(sum(b)/len(b),2))
