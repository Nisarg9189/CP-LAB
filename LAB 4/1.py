st = str(input("Enter the str: "))

def toggle_case(st):
    result = ""
    for char in st:
        if 'A'<= char <= 'Z':
            result += chr(ord(char) + 32)
            
        elif 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
            
        else:
            result += st
    return result
        
print(toggle_case(st))