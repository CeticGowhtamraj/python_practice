a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))
if(a>b):
    if(a>c):
        print("a is greatest")
    else:
        print("c is greatest")
elif(b>c):
    print("b is greatest")
else:
    print("c is greatest")
