with open("my file.txt", "r") as f1:
    lines1 = f1.readlines()
    with open("nisarg.txt", "r") as f2:
        lines2 = f2.readlines()
        with open("target.txt","w") as f3:
            max_len = max(len(lines1), len(lines2))
            for i in range(max_len):
                if i < len(lines1):
                    f3.write(lines1[i])
                if i < len(lines2):
                    f3.write(lines2[i])
f1.close()
f2.close()
f3.close()
