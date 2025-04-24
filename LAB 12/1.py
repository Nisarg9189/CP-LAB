class Complex:
    
    def __init__(self, real=0, img=0):
        self.real = real
        self.img = img
        
    def print_ans(self):
        print(f"{self.real} + {self.img}i")
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.img + other.img)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.img - other.img)
    
    def __mul__(self, other):
        return Complex(self.real * other.real, self.img * other.img)
    
    def __truediv__(self, other):
        denom = other.real**2 + other.img**2
        real_part = (self.real * other.real + self.img * other.img) / denom
        img_part = (self.img * other.real - self.real * other.img) / denom
        return Complex(real_part, img_part)
        
        
    

c1 = Complex(10, 10)
c2 = Complex(10, 10)
c3 = c1 + c2
c3.print_ans()
c4 = c1 - c2
c4.print_ans()
c5 = c1 * c2
c5.print_ans()
c6 = c1 / c2
c6.print_ans()