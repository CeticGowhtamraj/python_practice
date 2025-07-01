def rev(st):
    str=" "
    for i in st:
        str=i+str
    return str
st=input("enter the string:")
print("the reversed string is:",rev(st))
