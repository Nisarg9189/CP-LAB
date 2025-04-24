def factorial(n):
    fact = 1
    for i in range(1, n + 1):  # Loop from 1 to n
        fact *= i
    return fact

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def nPr(n, r):
    return factorial(n) // factorial(n - r)

# Take input from user
n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))

# Ensure r is not greater than n
if r > n:
    print("Invalid input: r should not be greater than n.")
else:
    # Print results
    print(f"{n}C{r} (Combination) = {nCr(n, r)}")
    print(f"{n}P{r} (Permutation) = {nPr(n, r)}")
