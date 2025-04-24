import random
l = []
for ele in range(31):
    a = random.randint(-10,10)
    l.append(a)
print(l)
pos = []
nev = []
for ele in l:
    if ele >=0:
        pos.append(ele)
    else:
        nev.append(ele)
print(pos)
print(nev)