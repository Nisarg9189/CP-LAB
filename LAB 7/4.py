input_string = input("Enter a string: ")


frequency_dict = {}


for char in input_string:
    
    if char in frequency_dict:
        frequency_dict[char] += 1
    else:
        frequency_dict[char] = 1
        
print("Character frequency dictionary:")
print(frequency_dict)