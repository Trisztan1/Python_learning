amount = 50

while amount > 0:
    print(f"Amount Due: {amount}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin == 25:
        amount -= 25
    elif insert_coin == 10:
        amount -= 10
    elif insert_coin == 5:
        amount -= 5

    print(f"Change Owed: {abs(amount)}")
    
