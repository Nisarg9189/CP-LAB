f = open("pdeu-csv-ms.csv", "a+")
rino = input("Enter Roll No.[Enter to end]:")
while rino:
    nm = input("Enter Name:")
    cp, maths, ch = input("Marks of CP, Maths and chemistry").split()
    f.write(rino+','+nm+','+cp+','+maths+','+ch+'\n')
    rino = input("Enter Roll No.[Enter to end]:")
f.close()