items=['ST','BD','BTL','CG','DD','HBT']
items1=['150,300','247,100','333,300','266,800','420,900','318,000']
l=len(items)
l1=len(items1)
# for i in range(l):
#     print(items[i])
# for i in range(l1):
#     print(items1[i])
# for i in range(l1):
#     if(items1[i]==max(items1)):
#         print("dan so nhieu nhat:",i)
#     elif(items1[i]==min(items1)):
#         print("dan so it nhat:",i)
for i in range(l):
    if(items1[i]==max(items1)):
        print("quan dan so nhieu nhat:",items[i])
    elif(items1[i]==min(items1)):
        print("quan dan so it nhat:",items[i])
        
