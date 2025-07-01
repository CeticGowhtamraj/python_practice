def palindrome(s):
    return s==s[::-1]
s=input("enter the string:")
ans=palindrome(s)
if ans:
    print("the given string palindrom")
else:
    print("it is not a palindrome")
    
