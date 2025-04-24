st = str(input("Enter a string:")).lower()
count = 0
def count_vowels(st,count):
    if "a" in st:
        count+=1
    if "e" in st:
        count+=1
    if "i" in st:
        count+=1
    if "o" in st:
        count+=1
    if "u" in st:
        count+=1
    return count
print(count_vowels(st,count))