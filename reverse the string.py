def rev1(st):
    str=" "
    for i in st:
        str=i+str
    return str
s=input("enter the string:")
print("the reversed string is:",rev1(s))

def palindrome(s):
     return s==s[::-1]
s=input("enter the string:")
ans=palindrome(s)
if ans:
    print("its is a palindrome")
else:
    print("it is not a palindrome")
