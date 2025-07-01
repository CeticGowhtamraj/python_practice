def rev1(st):
    str=" "
    for i in st:
        str=i+str
    return str
s=input("enter the string :")
print("reveresd string is :", rev1(s))
