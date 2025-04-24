f = open("pdeu-csv-ms.csv")
lines = f.readline()
while(lines != ""):
    print(lines)
    lines = f.readline()
f.close()