def reverse_list_recursive(lst):
    if len(lst) <= 1: 
        return lst
    return [lst[-1]] + reverse_list_recursive(lst[:-1])  


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
reversed_numbers = reverse_list_recursive(numbers)
print(f"Reversed list: {reversed_numbers}")
