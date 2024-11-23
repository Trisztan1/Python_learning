import random


def main():
    level = get_level()
    operator = get_arithmetics()
    n = 10
    chances = 3
    serial_number = int(1)
    score = int()

    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None, 
    }
    
    while n > 0:
        allow_scoring = True
        x = generate_integer(level)
        y = generate_integer(level)
        result = operations[operator](x,y)

        if result is None:
            continue
        
        while chances > 0:
            try:
                user_input = int(input(f"{serial_number}. {x} {operator} {y} = "))

                if result == user_input:
                    n -= 1
                    serial_number += 1
                    
                    if allow_scoring == True:
                         score += 1
                    break
                
                elif result != user_input:
                    allow_scoring = False
                    chances -= 1
                    print("EEE")

            except ValueError:
                allow_scoring = False
                chances -= 1
                print("EEE")
            
            if chances == 0:
                        n -= 1
                        serial_number += 1
                        chances = 3
                        print(f"{serial_number}. {x} {operator} {y} = {result}")
                        break
                

        
    print(f"Score: {score}")
        

                





def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1,2,3]:
                return level

        except ValueError:
            pass


def get_arithmetics():
    while True:
        try:
            operator = input("Operator: ").strip()

            if operator in ["+", "-", "*", "/"]:
                return operator
            else:
                print("It is not an arithmetic operator")
        
        except ValueError:
            print("It is not an arithmetic operator")

def generate_integer(level):
    
    if level == 1:
        x = random.randint(1, 9)
        return x
    elif level == 2:
        x = random.randint(10,99)
        return x
    elif level == 3:
        x = random.randint(100,999)
        return x


if __name__ == "__main__":
    main()