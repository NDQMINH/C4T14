# a=list(n)
# while True:
#     if a.isdigit():
#         print("Retype")
#     else:
#         print(n)
while True:
    n=input("enter a number:")
    if(n.isalpha()==True):
        print(n)
        break
    else:
        print("Retype")