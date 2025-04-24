n = int(input("Enter a number number: "))

def calculate_number_count(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    print(count)

calculate_number_count(n)

    