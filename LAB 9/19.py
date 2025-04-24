def string_length_recursive(s):
    if s == "":  
        return 0
    return 1 + string_length_recursive(s[1:])  

text = input("Enter a string: ")
length = string_length_recursive(text)
print(f"Length of the string '{text}' is {length}")
