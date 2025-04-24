l = []
def decimal_to_binary_recursive(n):
    if n == 0:
        return ""
    return decimal_to_binary_recursive(n // 2) + str(n % 2)

num = int(input("Enter a positive integer: "))
binary_equivalent = decimal_to_binary_recursive(num)
print(f"Binary equivalent of {num} is {binary_equivalent if binary_equivalent else '0'}")
