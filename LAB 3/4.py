st = str(input("Enter a string:"))
remove = str(input("Enter a to remove from str:"))

def remove_str(st,remove):
    if remove in st:
        st = st.replace(remove,"")
    return st
print(remove_str(st,remove))