import re
import sys

def main():
        print(convert(input("Hours: ").strip()))

def convert(s):
    # Old pattern not used any more
    patter_old = r"^(?P<time_1>\d) (?P<abbr_1>[AM|PM]{2}) to (?P<time_2>\d) (?P<abbr_2>[AM|PM]{2})$"

    pattern = r"^((?P<hour_1>\d{1,2})\:?(?P<minute_1>[0-5][0-9])?) (?P<abbr_1>AM|PM) to ((?P<hour_2>\d{1,2})\:?(?P<minute_2>[0-5][0-9])?) (?P<abbr_2>AM|PM)$"

    match = re.search(pattern, s)

    if not match:
        raise ValueError("Invalid time format")
    hour_1, hour_2 = int(match.group("hour_1")), int(match.group("hour_2"))
    minute_1, minute_2 = match.group("minute_1") or "00", match.group("minute_2") or "00"
    abbr_1, abbr_2 = match.group("abbr_1"), match.group("abbr_2")

    if not (1 <= hour_1 <= 12) or not (1 <= hour_2 <= 12):
        raise ValueError("Invalid time format")
    if not (0 <= int(minute_1) <= 59) or not (0 <= int(minute_2) <= 59):
        raise ValueError("Invalid time format")

    hour_1 = convert_hour(hour_1, abbr_1)
    hour_2 = convert_hour(hour_2, abbr_2)

    return f"{hour_1:02}:{minute_1} to {hour_2:02}:{minute_2}"

def convert_hour(hour, abbr):
    if abbr == "PM":
        # hour = 12 if hour == 12 else hour + 12
        return 12 if hour == 12 else hour + 12
    else:
        # hour = 0 if hour == 12 else hour
        return 0 if hour == 12 else hour

if __name__ == "__main__":
    main()