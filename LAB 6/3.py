from datetime import datetime

date_tuple1 = ("12/02/2022",)  
date_tuple2 = ("25/02/2024",)  


date1 = datetime.strptime(date_tuple1[0], "%d/%m/%Y")
date2 = datetime.strptime(date_tuple2[0], "%d/%m/%Y")

total_days = abs((date2 - date1).days)

print("Total Difference in Days:", total_days)
