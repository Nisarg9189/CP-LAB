def fun():
    print("This is fun()")

def disp():
    print("This is disp()")

def msg():
    print("This is msg()")

func_list = [fun, disp, msg]

for f in func_list:
    f()
