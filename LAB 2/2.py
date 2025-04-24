a = int(input("Enter a number a: "))
b = int(input("Enter a number b: "))
c = int(input("Enter a number c: "))
def smallest_largest(a, b, c):
    if a > b and a > c:
        print(f"{a} is greater than {b} and {c}")
    elif b > a and b > c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c} is greater than {a} and {b}")

smallest_largest(a, b, c)