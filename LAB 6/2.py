l1 = [(58,"prince",19.0),(57,"het",19.0),(65,"nisarg",19.0)]
roll = []
name = []
age = []

for ele in l1:
    if isinstance(ele,tuple):
        for i in ele:
            if isinstance(i,int):
                roll.append(i)
            elif isinstance(i,str):
                name.append(i)
            elif isinstance(i,float):
                age.append(i)
                
print(f"roll = {roll}")
print(f"name = {name}")
print(f" age = {age}")