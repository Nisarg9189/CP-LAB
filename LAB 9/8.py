def convert(s):
    s = set(s.lower())
    s = list(s)
    s.sort()
    if " "in s:
        s.remove(" ")
    return "".join(s)
print(convert("Nisarg"))
    