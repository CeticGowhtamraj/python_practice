n=int(input("enter the number:"))
first=0
second=1
for i in range(n):
    print(first,end=" ")
    temp=first
    first=second
    second=temp+first
