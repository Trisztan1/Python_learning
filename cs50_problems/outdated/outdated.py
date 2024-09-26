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

def main(): # 10 December, 1815
    while True:
        user_input = input("Date: ").strip()
        cleaned_input = user_input.replace(",", "/").replace(" ", "/")
        final_input = cleaned_input.replace("//", "/")
        m,d,y = final_input.split("/")

        if m.isdigit():
            m = int(m)
        else:
            m = months.index(m.capitalize()) + 1

        if d.isalpha():
            continue

        d = int(d)
        y = int(y)

        if m < 1 or m > 12 or d > 31:
            continue
        else:
            print(f"{y}-{m:02}-{d:02}")
            break

main()
