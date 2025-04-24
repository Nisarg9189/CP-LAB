def sanitize_list_recursive(lst, index=0):
    if index == len(lst):  
        return lst
    if lst[index] < 0:  
        lst[index] = 0
    return sanitize_list_recursive(lst, index + 1)  


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sanitize_list_recursive(numbers)
print(f"Sanitized list: {numbers}")
