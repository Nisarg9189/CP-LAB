n = int(input("Enter the number: "))

def prime(n):
    count = 0
    for i in range(2,n):
        if n%i==0:
            count = count + 1
    if count==0:
        print("prime")
    else:
        print("not prime")
prime(n)
a = int(input("enter the number: "))
def perfact(a):
    count = 0
    for i in range(1,int(n/2 + 1)):
        if a%i==0:
            count+=i
    if count == a:
        print("number is perfect")
    else:
        print("number is not perfact")
perfact(a)
z = int(input("inter the number: "))
def armstrog(z):
    l = [ ]
    original = z
    sum = 0
    while z!=0:
        l.append(z%10)
        z //= 10
        
    for digit in l:
        power = pow(digit,len(l))
        sum+=power
    
    if sum == original:
        print("armstrong")
    else:
        print("not armstrong")
    
    
armstrog(z)

def is_palindrome(e):
    original = str(e)  
    reverse = original[::-1]  
    
    if original == reverse:
        print("Palindrome")
    else:
        print("Not a palindrome")

e = int(input("Enter a number: "))
is_palindrome(e)
b = int(input("Enter the number: "))
def automor(b):
    squre = b**2
    if (str(squre).endswith(str(b))):
        print("automorphic")
    else:
        print("no automorphic")

automor(b)
    