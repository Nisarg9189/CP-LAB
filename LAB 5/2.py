import random
l = []
for ele in range(10):
    a = random.randint(1,10)
    l.append(a)
print(l)
user = int(input("Enter the number:"))
for index, ele in enumerate(l):
    if user == ele:
        print(f"Index {index},element {ele}")
        continue
        