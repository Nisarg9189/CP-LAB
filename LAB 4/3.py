
st = str(input("Enter the string: ")).lower()

def alnum(st):
    count_al = 0
    count_digit = 0
    for char in st:
        if 'a' <= char <= 'z':
            count_al = count_al + 1
    
        elif '0'<= char <= '9':
            count_digit = count_digit + 1
    return count_al,count_digit
    
        
print(alnum(st))
             
            
            
            