def compute(*n):
    for i in n:
        n1 = str(i)
        n2 = (n1)*2
        n3 = (n1)*3
        n4 = (n1)*4
        
        sum = int(n1) + int(n2) + int(n3) + int(n4)
        print(sum)

compute(4,5,6,7)