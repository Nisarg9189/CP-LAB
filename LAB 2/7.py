year = int(input("Enter a year: "))

def leep(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leep year")
            else:
                print(f"{year} is not a leep year")
        else:
            print(f"{year} is a leep year")
    else:
        print(f"{year} is not a leep year")
            
leep(year)