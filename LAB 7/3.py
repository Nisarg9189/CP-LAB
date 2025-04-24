# Input dictionary with tuple keys
d1 = {
    (1, 28): 5000,
    (1, 30): 2000,
    (2, 65): 3000
}

# Output dictionary to store max, min, and total values for each first key
d2 = {}

# Loop through dictionary d1
for k, v in d1.items():
    category = k[0]  # Extract first element of tuple as key
    index = k[1]  # Extract second element (not used in d2)
    
    print(category, index, v)  # Debugging print

    # If category is not in d2, initialize its values
    if category not in d2:
        d2[category] = {"Max": v, "Min": v, "Total": v}
    else:
        # Update Max if the new value is greater
        d2[category]["Max"] = max(d2[category]["Max"], v)
        # Update Min if the new value is smaller
        d2[category]["Min"] = min(d2[category]["Min"], v)
        # Update Total by adding the new value
        d2[category]["Total"] += v

# Print the final dictionary after processing
print(d2)
