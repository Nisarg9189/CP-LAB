a = float(input("Enter the angle a: "))
b = float(input("Enter the angle b: "))
c = float(input("Enter the angle c: "))

def triangle(a, b, c):
    if a + b + c == 180:
        print("true triangle")
    else:
        print("false triangle")
        
triangle(a, b, c)