class Date:
    def __init__(self, day:int, month:int, year:int):
        self.day = day
        self.month = month
        self.year = year
    
    def __eq__(self, other):
        return (self.day == other.day and self.month == other.month and self.year == other.year)
    
    
d1 = Date(1, 2, 2023)
d2 = Date(1, 2, 2023)
print(d1 == d2)  
d3 = Date(1, 3, 2023)
print(d1 == d3) 