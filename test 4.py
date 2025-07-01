def fact(n):
    if n==0 or n==1:
        return 1
    else:
         return n*fact(n-1)
n=int(input("enter the number:"))
print("the factiorial of the given numbr:", fact(n))
      
