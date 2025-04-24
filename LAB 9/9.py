def count_alpha_digits(s):
    l = ["1","2","3","4","5","6","7","8","9"]
    v = []
    c = []
    for i in range(97, 123):
        c.append(chr(i))
    for i in s:
        v.append(i.lower())
    count_digits = 0
    count_alpha = 0
    for ele1 in v:
        for ele2 in l:
            if ele1 in ele2:
                count_digits +=1
    for ele3 in c:
        for ele4 in v:
            if ele3 in ele4:
                count_alpha+=1
    return count_digits,count_alpha
count_digits,count_alpha = count_alpha_digits("Nisarg9189")
d = {"digits":count_digits,
     "alpha":count_alpha}
print(d)
            
            
    