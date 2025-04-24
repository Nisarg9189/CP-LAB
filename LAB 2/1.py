a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
def smallest_largest(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")
        
smallest_largest(a, b)