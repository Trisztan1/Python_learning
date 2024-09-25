grocery_list = {}

def main():
    while True:
        try:
            user_input = input("").lower().strip()
            if user_input not in grocery_list:
                grocery_list[user_input] = 1
            else:
                grocery_list[user_input] += 1

        except EOFError:
            sorted_list = sorted(grocery_list)
            for item in sorted_list:
                print(grocery_list[item], item.upper())
            break

main()