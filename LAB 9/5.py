def ispangram(l):
    a = []
    for ele in range(97, 123):
        a.append(chr(ele))
    b = set(l.lower())
    for ele in a:
        if ele not in b:
            return False
    return True
n = set("Crazy ,Fredrick bought many very exquisite opal jewels")
n = str(n)
print(ispangram(n))
print(ispangram("Nisarg"))
    