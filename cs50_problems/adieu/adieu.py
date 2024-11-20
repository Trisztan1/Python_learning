import inflect

def main():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            user_input = input("Name: ").strip()
            name_list.append(user_input)

        except EOFError:
            name_list = p.join(name_list)
            print(f"Adieu, adieu, to {name_list}")
            break

main()

