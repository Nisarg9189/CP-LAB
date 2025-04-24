def number_to_words(n):
    words = ["zero", "one", "two", "three", "four", "five", 
             "six", "seven", "eight", "nine", "ten", "eleven", 
             "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    
    if 0 <= n <= 19:
        return words[n]
    else:
        return False


number = int(input("Enter a number between 0 and 19: "))
print(f"{number} → {number_to_words(number)}")
