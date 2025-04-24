import random

def duplicate(lst):
    return [ele for ele in l if l.count(ele)==1]
l = []
for ele in range(51):
    a = random.randint(1,30)
    l.append(a)
print(duplicate(l))
           
    
