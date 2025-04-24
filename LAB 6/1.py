t1 = (("nisarg","prince"),"jensy","nency",("mahir","vijay"))
boy_sum = 0
girl_sum = 0
for ele in t1:
    if isinstance(ele,tuple):
        for i in ele:
            boy_sum+=1
        #print(len(ele))
    else:
        girl_sum += 1
print(f"girl = {girl_sum}")
print(f"boys = {boy_sum}")     