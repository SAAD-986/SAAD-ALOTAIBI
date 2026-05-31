due = 50
while due > 0:   
    print(f"Amount Due: {due}")
    user_input = input("Insert Coin: ")      
    try:
        coin = int(user_input)
    except ValueError:
        print("Please insert a valid integer coin")
        continue  
    if coin in [25, 10, 5]:
        due = due - coin
    else:
        print(f"Coin not accepted. Returning {coin} cents")  
change_owed = abs(due)
print(f"Change Owed: {change_owed}")