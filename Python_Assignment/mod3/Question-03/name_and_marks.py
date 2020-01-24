s=input('enter the name and marks').split(',')
k=list(map(int,s[1:]))
print(s[0],'obtained',sum(k[1:-3]),'marks out of 500 in theory and',sum(k[-3: ]),'marks in practical out of 150 and successfully passed with ',"{0:.2f}".format((sum(k[ : ]))*100/650),'percentage ,may many congratulations!!')
