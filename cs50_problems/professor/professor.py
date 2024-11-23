import random


def main():
    level = get_level()
    n = 10
    chances = 3
    serial_number = int(1)
    score = int()
    
    while n > 0:
        allow_scoring = True
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        
        while chances > 0:
            try:
                user_input = int(input(f"{serial_number}. {x} + {y} = "))

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
                        print(f"{x} + {y} = {result}")
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