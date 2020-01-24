s=input('Enter the full path of the file')

print(((s.split('/')[-1]).split('.'))[0],end='.pdf')
