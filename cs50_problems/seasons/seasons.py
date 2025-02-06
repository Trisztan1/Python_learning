from datetime import date, timedelta
import sys
import re
import inflect

def main():
    try:
        user_input = input("Date of Birth: ").strip()
        today = input("What is the current date: ").strip()
        print(date_to_minutes(user_input, today))
    except ValueError as e:
        sys.exit(e)

def is_date_correct(input):
    pattern = r"^([0-9][0-9][0-9][0-9])-([0-1][0-2]|0[0-9])-([0-2][0-9]|3[0-1])$"
    match = re.search(pattern, input)
    if not match:
        raise ValueError("Invalid format, use YYYY-MM-DD")
    return [int(match.group(1)), int(match.group(2)), int(match.group(3))]

def date_to_minutes(input, current_date=None):
    p = inflect.engine()
    year, month, day = is_date_correct(input)
    d = date(year, month, day)
    try:
        c_year, c_month, c_day = is_date_correct(current_date)
        current_date = date(c_year, c_month, c_day)
    except ValueError:
        current_date = date.today()

    all_days = current_date - d
    minutes = all_days.days * 24 * 60
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()