vcF = ["1.vcf", "2.vcf","3.vcf"]
for ele in vcF:
    with open(ele, "w") as f:
        name = input("enter the name:")
        contact = input("enter the contact number:")
        f.write(f"Begin{{\nName : {name}\nContact : {int(contact)}\n}}End")
f.close()