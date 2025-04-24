import random

first = []
for i in range(6):
    a = random.randint(1,10)
    first.append(a)
print(first)
second = []
for i in range(6):
    b = random.randint(1,10)
    second.append(b)
print(second)
third = []
def change(first,second):
    for ele in first:
        if ele not in second:
            third.append(ele)
    return third
print(change(first,second))