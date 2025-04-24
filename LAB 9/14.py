def count_vowels_recursive(s, index=0):
    vowels = "aeiouAEIOU"
    if index == len(s):  
        return 0
    return (1 if s[index] in vowels else 0) + count_vowels_recursive(s, index + 1)


text = input("Enter a string: ")
vowel_count = count_vowels_recursive(text)
print(f"Number of vowels in '{text}' is {vowel_count}")

