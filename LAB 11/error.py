while(True):
    try:
        a = int(input("Enter the number:"))
        if type(a) == int:
            break
    except ValueError:
        print("Type error")