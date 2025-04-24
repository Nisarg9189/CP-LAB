gross_salary = float(input("Enter the gross salary:"))
allowances = float(input("Enter the allowances:"))
deductions = float(input("Enter the deductions:"))
dedu_cation = 0.3*gross_salary
net_salary = gross_salary + (allowances)*0.1 - dedu_cation
print(f"Net salary = {net_salary}")