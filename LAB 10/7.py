with open("file.txt", "r") as f1:
    data = f1.read()
    with open("donkey.txt", "w") as f2:
        f2.write(data.upper())
f2.close()
f1.close()