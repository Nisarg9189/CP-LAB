n = int(input("Enter a number n: "))

def div_by_ten(n):
    if n % 10 == 0:
        return True
    else:
        return False
print(div_by_ten(n))