amount = 50
valid_coin = (5, 10, 25)

while amount > 0:
    print(f"Amount Due: {amount}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in valid_coin:
        amount -= insert_coin
    
    if amount < 0:
        print(f"Change Owed: {abs(amount)}")