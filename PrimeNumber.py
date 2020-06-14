while 1==1:
    no=int(input("enter a no  "))
    start=1
    while start<no/2:
        if(no%start==0):
            print("{} is not a prime no".format(no))
            break
        start=start+1
    else:print("{} is a prime no".format(no))

    isexit=input("do want to exit  ")
    if(isexit=="y" or isexit=="yes" ):
        break


