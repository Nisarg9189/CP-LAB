def prime_factor(n,divisor=2):
    if n == 1:
        return []
    
    if n % divisor == 0:
        return [divisor] + prime_factor(n // divisor, divisor)
    
    return prime_factor(n, divisor + 1)

n = int(input("Enter the value:"))
print(prime_factor(n))