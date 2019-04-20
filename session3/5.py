
# test=float("inf")
from random import *
x=int(randint(0,1000000))
y=int(randint(0,1000000))
re=int(randint(0,10000000))
kqs=int(randint(0,100000))
dem=0
op=choice(['+','-','*','/'])
if op=='+':
    re=x+y
    print(re,"=",x,"+",y)
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True):
        # print(re,"=",x,"+",y) 
        print("TRUE")
    if(b==True): 
        # print(re,"=",x,"+",y)
        print("GAME OVER")
elif op=='-':
    re=x-y
    print(re,"=",x,"-",y) 
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True):
        # print(re,"=",x,"-",y) 
        print("TRUE")
    if(b==True): 
        # print(re,"=",x,"-",y) 
        print("GAME OVER")
elif op=='*':
    re=x*y
    print(re,"=",x,"*",y)
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True): 
        # print(re,"=",x,"*",y)
        print("TRUE")
    if(b==True):
        # print(re,"=",x,"*",y)
        print("GAME OVER")
elif op=='/':
    re=x/y
    print(re,"=",x,"/",y)
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True):
        # print(re,"=",x,"/",y)
        print("TRUE")
    if(b==True): 
        # print(re,"=",x,"/",y)
        print("GAME OVER")
if op=='+':
    re=x+y+kqs
    print(re,"=",x,"+",y)
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True):
        # print(re,"=",x,"+",y) 
        print("GAME OVER")
    if(b==True): 
        # print(re,"=",x,"+",y)
        print("TRUE")
elif op=='-':
    re=x-y+kqs
    print(re,"=",x,"-",y) 
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True):
        # print(re,"=",x,"-",y) 
        print("GAME OVER")
    if(b==True): 
        # print(re,"=",x,"-",y) 
        print("TRUE")
elif op=='*':
    re=x*y
    print(re,"=",x,"*",y)
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True): 
        # print(re,"=",x,"*",y)
        print("GAME OVER")
    if(b==True):
        # print(re,"=",x,"*",y)
        print("TRUE")
elif op=='/':
    re=x/y
    print(re,"=",x,"/",y)
    a=bool(input("TypeYES:"))
    b=bool(input("TypeNO:"))
    if(a==True):
        # print(re,"=",x,"/",y)
        print("GAME OVER")
    if(b==True): 
        # print(re,"=",x,"/",y)
        print("TRUE")