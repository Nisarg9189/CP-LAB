import csv
employees = [
    ["empcode", "empname", "Date of Joining", "Salary"],
    [101, "Nisarg", "2023-08-01", 50000],
    [102, "Rahul", "2022-12-15", 60000]
]
with open("employee.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(employees)

with open("employee.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
