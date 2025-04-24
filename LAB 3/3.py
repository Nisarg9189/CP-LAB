st = str(input("Enter a string:"))

check = str(input("Enter a to check str:"))

def check_str(st,check):
    if check in st:
        return "Yes"
    else:
        return "No"
print(check_str(st,check))