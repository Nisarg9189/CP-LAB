import math

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def sin_taylor(degrees, terms=10):
    x = degrees * (3.14159 / 180)  
    sin_x = 0

    for n in range(terms):
        term = ((-1)**n) * (x**(2*n + 1)) / factorial(2*n + 1)
        sin_x += term

    return sin_x


angle_deg = float(input("Enter angle in degrees: "))
approx_sin = sin_taylor(angle_deg)
print(f"Approximate sin({angle_deg}) = {approx_sin}")
print(f"Actual sin({angle_deg}) = {math.sin(angle_deg * math.pi / 180)}")
