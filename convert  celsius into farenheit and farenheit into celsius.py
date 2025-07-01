print("1. celscius to farenheit \n 2. fahrenheit to celsius")
ch=int(input("enter your choice:"))
if(ch==1):
    c=int(input("enter the temperature in faherinheit:"))
    f=(c*(9/5))+32
    print("the temperature in farenhiet :",f)
elif(ch==2):
       f=int(input("enter the  temperature in celcius:"))
       c=(f-32)*(5/9)
       print("the temperature in celsius:",c)
else:
    print("wrong number")
    
