m = float(input("Enter the maths marks: "))
abm = str(input("student is absent in maths or not: "))
p = float(input("Enter the physics marks: "))
abp = str(input("student is absent in physics or not: "))
c = float(input("Enter the chemistry marks: "))
abc = str(input("student is absent in chemistry or not: "))
print(f"total = {m + p + c}")
print(f"avg = {(m + p + c) / 3}")
def maths(m,abm):
    if(m<=39):
        print("Fail in maths Grade:F")
    elif("absent".lower() in abm):
        print("absent")
    elif(40<=m<=44):
        print("maths:P")
    elif(45<=m<=49):
        print("maths:C")
    elif(50<=m<=54):
        print("maths:B")
    elif(55<=m<=59):
        print("maths:B+")
    elif(60<=m<=69):
        print("maths:A")
    elif(70<=m<=79):
        print("maths:A+")
    elif(80<=m<=100):
        print("maths:O")

def physics(p,amp):
    if(p<=39):
        print("Fail in physics Grade:F")
    elif("absent".lower() in abp):
        print("absent")
    elif(40<=p<=44):
        print("physics:P")
    elif(45<=p<=49):    
        print("physics:C")
    elif(50<=p<=54):
        print("physics:B")
    elif(55<=p<=59):
        print("physics:B+")
    elif(60<=p<=69):
        print("physics:A")
    elif(70<=p<=79):
        print("physics:A+")
    elif(80<=p<=100):
        print("physics:O")
def chemistry(c,abc):
    if(c<=39):
        print("Fail in chemistry Grade:F")
    elif("absent".lower() in abc):
        print("absent")
    elif(40<=c<=44):
        print("chemistry:P")
    elif(45<=c<=49):
        print("chemistry:C")
    elif(50<=c<=54):
        print("chemistry:B")
    elif(55<=c<=59):
        print("chemistry:B+")
    elif(60<=c<=69):
        print("chemistry:A")
    elif(70<=c<=79):
        print("chemistry:A+")
    elif(80<=c<=100):
        print("chemistry:O")

maths(m,abm)
physics(p,abp)
chemistry(c,abc)