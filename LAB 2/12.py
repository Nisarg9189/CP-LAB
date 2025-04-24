import math
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
radius = float(input("Enter the radius of the circle: "))

x1 = float(input("Enter the value of x1: "))
y1 = float(input("Enter the value of y2: "))

def distance(x, y, x1, y1):
    distance = (pow(x1 - x, 2) + pow(y1 - y, 2))**0.5
    
    if distance == radius:
        print("on the circle")
    elif distance > radius:
        print("outside the circle")
    else:
        print("inside the circle")
distance(x, y, x1, y1)
    



    