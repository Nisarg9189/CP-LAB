def avg(n):
    if n==0:
        return 0
    
    return avg(n-1)+n
n = int(input("eneter the num:"))
sum = avg(n)
print(sum)
av = sum/n
print(av)