bytes = float(input("Enter the amount in bytes: "))
kb = bytes / 1024
mb = kb / 1024
gb = mb / 1024
print(f"{bytes} bytes = {kb} kb = {mb} mb = {gb} gb")