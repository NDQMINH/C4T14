# items=[45, 67, 56, 78]
# l=len(items)
# k=sorted(items,reverse=True)
# for i,item in enumerate(k):
#     print(i+1,".",item)
# items=[45, 67, 56, 78]
# l=len(items)
# items.append(70)
# k=sorted(items,reverse=True)
# for i,item in enumerate(k):
#     print(i+1,".",item)
items=[45, 67, 56, 78]
l=len(items)
items.append(70)
items.append(76)
k=sorted(items,reverse=True)
k.pop(5)
for i,item in enumerate(k):
    print(i+1,".",item)
   