s = {"Anisarg","Bjensy"}
s1 = set()
s2 = set()
for ele in s:
    if ele.lower().startswith("a"):
        s1.add(ele)
    else:
        s2.add(ele)
print(s1)
print(s2)