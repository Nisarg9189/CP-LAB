import random
odd = []
for i in range(1,6):
    a = random.choice(range(1,10,2))
    odd.append(a)
#odd.sort()
even = []  
for i in range(1,5):
    b = random.randint(1,10)*2
    even.append(b)
#even.sort()
print(odd)
print(even)
odd[2] = even 
print(odd)
nested =[]
for ele in odd:
    if isinstance(ele ,list):
        nested.extend(ele)
    else:
        nested.append(ele)

nested.sort()
print(nested)

