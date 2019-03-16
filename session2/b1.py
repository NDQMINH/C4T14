a=input("")
b=input("")
int_a = int(a)
int_b=int(b)
while b!=0:
    r=a%b
    a=b
    b=r

print(int_a)