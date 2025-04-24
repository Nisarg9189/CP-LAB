lst = ['madam', 'Python', "malayalam", 12321]

for item in lst:
    s = str(item).lower()
    if s == s[::-1]:
        print(f"{item} is a palindrome")
