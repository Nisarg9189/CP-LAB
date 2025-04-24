import random

numbers = random.sample(range(-15, 16), 10)  # ensures unique values
squares = [x**2 for x in numbers]

print("Random numbers:", numbers)
print("Squares:", squares)
