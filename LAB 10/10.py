l = ["an","the","a"]
with open("text.txt", "r") as f1:
    data = f1.read()
with open("new.txt", "w") as f2:
    for i in l:
        data = data.lower().replace(i, "")
    f2.write(data)
f1.close()
f2.close()
        