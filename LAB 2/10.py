length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))
def check(l,w):
    area = l*w
    perimeter = 2*(l+w)
    print(f"Area of rectangle = {area}")
    print(f"Perimeter of rectangle = {perimeter}")
    if area > perimeter:
        return "Area is greater than perimeter"
    else:
        return "Perimeter is greater than area"
print(check(length, width))
