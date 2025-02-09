import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
         return "🍪" * self.size if self.size > 0 else "Empty jar"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies exceeds capacity!")
        if n < 0:
            raise ValueError("Deposit number can't be negative")
        self.size = self.size + n
        return self.size

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("There aren't enough cookies in the jar!")
        if n < 0:
            raise ValueError("Withdraw number can't be negative")
        self.size = self.size - n
        return self.size

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a non negative integer")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("There aren't enough cookies in the jar!")
        self._size = size


def main():
    answers = ["--deposit/-d", "--withdraw/-w", "--capacity/-c", "--set_capacity/-sc", "--size/-s"]
    jar = Jar()

    try:
        while True:
            user_input = input("Give me an input or ask [--help/-h]: ").lower()
            if user_input in ["--help", "-h"]:
                print(f"Choose from the followings: {answers}")
            elif user_input in ["--deposit", "-d"]:
                jar.deposit(int(input("How much cookies would you like to deposit: ")))
            elif user_input in ["--withdraw", "-w"]:
                jar.withdraw(int(input("How much cookies would you like to withdraw: ")))
            elif user_input in ["--capacity", "-c"]:
                print(f"The full capacity of the jar is {jar.capacity}")
            elif user_input in ["--set_capacity", "-sc"]:
                jar.capacity = int(input("Set the maximum capacity: "))
            elif user_input in ["--size", "-s"]:
                print(jar)
            else:
                print("I do not understand")
    except EOFError:
        sys.exit("Goodbye")
    except ValueError as e:
        sys.exit(e)



if __name__ == "__main__":
    main()