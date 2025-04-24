import random
s = set()
count = 0
for i in range(11):
    s.add(random.randint(15, 45))
for ele in s:
    if ele<30:
        count = count + 1
to_remove = [ele for ele in s if ele>35]
#print(to_remove)
for ele in to_remove:
    s.discard(ele)
print(s)
print(count)

    