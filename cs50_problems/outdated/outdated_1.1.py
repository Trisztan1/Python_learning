def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            user_input = input("Date: ").strip()
            if "/" in user_input:
                month, day, year = user_input.split("/")
                if month in months:
                    continue
                else:
                    month = int(month)
                day = int(day)
                if month > 12 or day > 31:
                    continue
                year = int(year)
                print(f"{year}-{month:02}-{day:02}")
                break
            elif " " in user_input:
                if user_input[0:1].isdigit():
                    continue
                month_day, year = user_input.split(",")
                month, day = month_day.split(" ")
                year = int(year)
                month = months.index(month) + 1
                day = int(day)
                if month > 12 or day > 31:
                    continue
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        except EOFError:
            break
        except ValueError:
            pass


main()