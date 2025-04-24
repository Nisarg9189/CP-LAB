def print_24_hours():
    for hour in range(24):  # Loop from 0 to 23
        if hour == 0:
            print("12 Midnight")  # 0:00 = Midnight
        elif hour == 12:
            print("12 Noon")  # 12:00 = Noon
        elif hour < 12:
            print(f"{hour} AM")  # 1 to 11 AM
        else:
            print(f"{hour - 12} PM")  # 1 to 11 PM

print_24_hours()
