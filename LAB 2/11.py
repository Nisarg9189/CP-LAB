x1 = float(input("Enter the value of x1: "))
y1 = float(input("Enter the value of y1: "))

x2 = float(input("Enter the value of x2: "))
y2 = float(input("Enter the value of y2: "))

x3 = float(input("Enter the value of x3: "))
y3 = float(input("Enter the value of y3: "))

def straight_line(x1, y1, x2, y2, x3, y3):
    if (y3 - y2) * (x2 - x1) == (y2 - y1) * (x3 - x2):
        return True
    else:
        return False
print(straight_line(x1, y1, x2, y2, x3, y3))