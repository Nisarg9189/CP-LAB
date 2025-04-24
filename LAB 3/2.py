st = str(input("Enter a string:"))
result = ""
def lower_case(st,result):
    if "A" <= st <= "Z":
        result = st.swapcase()
    return result
print(lower_case(st,result))




