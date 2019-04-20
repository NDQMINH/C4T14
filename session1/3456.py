from random import randint
n=randint(0,100)
if n<=30:
    print("Rainy")
elif n>=30 and n<=60:
    print("Cloudy")
elif n>=60:
    print("Sunny")
    