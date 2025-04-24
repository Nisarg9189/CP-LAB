d1 = {}
f = open("pdeu-csv-ms.csv")
lines = f.readlines()
for line in lines:
    parts = line.strip().split(",")
    
    if(len(parts)>=2):
        key = parts[0]
        value = parts[1:]
        d1[key] = value
f.close()
print(d1)
