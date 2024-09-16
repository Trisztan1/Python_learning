user_input = input("Expression: ")
x, y, z = user_input.split()
x = float(x) 
z = float(z)

match y:
    case y if y == "+":
        print(x + z)
    case y if  y == "-":
        print(x - z)
    case y if y == "*":
        print(x * z)
    case y if y == "/":
        print(x / z)