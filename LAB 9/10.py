def frequency():
    l = []
    input_string = input("Enter a string: ")
    for ele in input_string:
        l.append(ele)
    l.sort()
    frequency_dict = {}
    for char in l:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict
print(frequency())
