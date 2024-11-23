import calendar

def generate_calendar(year, month):
    cal = calendar.monthcalendar(year, month)
    month_name = calendar.month_name[month]

    print(f"Calendar for {month_name} {year}:")
    print(" Mo Tu We Th Fr Sa Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2} ", end=" ")

        print()

if __name__ == "__main__":
    year = int(input("Enter the year: "))
    month = int(input("Enter the month (1-12): "))

    generate_calendar(year, month)