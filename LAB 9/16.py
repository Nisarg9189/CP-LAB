def power_recursive(a, b):
    if b == 0:  
        return 1
    return a * power_recursive(a, b - 1)  

a = int(input("Enter the base (a): "))
b = int(input("Enter the exponent (b): "))
result = power_recursive(a, b)
print(f"{a}^{b} = {result}")
