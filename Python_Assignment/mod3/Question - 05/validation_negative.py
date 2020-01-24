while(True):
    wc=input('Enter the Wholesale cost')
    if '-' in str(wc):
        break
    else:
        print("Retail cost ",int(wc)*0.5)
    ch=input('Press 1 to continue ,Press 2 to exit')
    if(ch==2):
        break
