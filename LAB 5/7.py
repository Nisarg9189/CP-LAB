stack = []

while True:
    print("1 for append")
    print("2 for pop")
    print("3 for exit")
    
    user = input("choice the operation:")
    if user == '1':
        a = input("Enter the value:")
        stack.append(a)
        print(f"append stack = {stack}")
    
    elif user == '2':
        if stack: 
            stack.pop()
            print(f"pop stack = {stack}")
        else:
            print("stack is empty")
    
    elif user == '3':
        print("operation over")
        break
    else:
        print("Invalid Input")