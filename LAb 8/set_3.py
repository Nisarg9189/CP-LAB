s = set()
for i in range(5):
    a = input("Enter a name: ")
    s.add(a)
old_name = "x"
new_name = "m"
if old_name in s:
    s.remove(old_name)
    s.add(new_name)
else:
    print("Name not found")
name_to_remove = ["x","y"]
for name in name_to_remove:
    s.discard(name)
print(s)