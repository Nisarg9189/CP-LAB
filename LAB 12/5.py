from datetime import datetime, timedelta

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"

    def __add__(self, other):
        return Time(self.hour + other.hour, 
                    self.minute + other.minute, 
                    self.second + other.second)
    
    def __sub__(self, other):
        return Time(self.hour - other.hour, 
                    self.minute - other.minute, 
                    self.second - other.second)
    
    def __gt__(self, other):
        return (self.hour, self.minute, self.second) > (other.hour, other.minute, other.second)

    def Total_Min(self):
        return self.hour * 60 + self.minute + self.second / 60

    def Duration(self, other):
        duration = abs(self.Total_Min() - other.Total_Min())
        return (f"{duration} minutes")
    
# Example usage
t1 = Time(2, 30, 45)
t2 = Time(1, 45, 30)
print("Time 1:", t1)
print("Time 2:", t2)
print("Addition:", t1 + t2)
print("Subtraction:", t1 - t2)
print("Greater than:", t1 > t2)
print("Total Minutes of Time 1:", t1.Total_Min())
print("Total Minutes of Time 2:", t2.Total_Min())
print("Duration between Time 1 and Time 2:", t1.Duration(t2))