def inter(a,b):
    a = set(a)
    b = set(b)
    a = list(a)
    b = list(b)
    c = []
    
    for i in a:
        for j in b:
            if(i==j):
                c.append(i)
    return c
a = [1,2]
b = [0,1,3,2]
print(inter(a,b))