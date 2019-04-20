# n=int(input("enter a number:"))
# if n>13:
#     print("YES")
# else:
#     print("NO")
# n=int(input("enter a number:"))
# if n%2==0:
#     print("YES")
# else:
#     print("NO")
n=int(input("enter a month:"))
if n<1 or n>12:
    print("Error")
elif n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("31")
else:
    print("30")