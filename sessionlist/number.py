number=[5, 1, 8, 92, 7, 30]
l=len(number)
for i in range(l):
    if int((number[i])%2==0):
        print(number[i], end=' ',sep=',')
