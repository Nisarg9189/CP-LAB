vcF = ["4.vcf", "5.vcf"]
with open("homework.csv", "r") as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
            parts = line.strip().split(",")
            if(len(parts)>=2):
                key = parts[0]
                value = parts[1:]
                with open(vcF[i], "w") as p:
                   p.write(f"Begin{{\nName : {key}\nContact : {''.join(value)}\n}}End")
p.close()
f.close()
                
   