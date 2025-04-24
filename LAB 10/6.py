import os

if "extra"not in "/Users/nisargpatel/Python/File I:O":
    os.makedirs("/Users/nisargpatel/Python/File I:O/extra")

with open("file.txt", "r") as f1:
    data = f1.read()
    print(data)
    with open("/Users/nisargpatel/Python/File I:O/extra/extra.txt", "w") as f2:
        f2.write(data)
f2.close()
f1.close()
    
    
    