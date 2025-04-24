def count_lower_upper(l):
    lower = 0
    upper = 0
    for ele in l:
        if (ele>="a" and ele<="z"):
            lower+=1
        else:
            upper+=1
    return lower,upper
input_string = input("Enter a string: ")
lower,upper = count_lower_upper(input_string)
dict = {"lower":lower,"upper":upper}
print(dict)
            
            