def main():
    ...
    user_input = input("What time is it? ")
    time = convert(user_input)
    if 18 <= time <= 19:
        print("dinner time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 7 <= time <= 8:
        print("breakfast time")
   


def convert(time):
    ...
    x,y = time.split(":")
    hours = int(x)
    minutes = float(y)
    minutes = minutes / 60
    return hours + minutes
    


if __name__ == "__main__":
    main()