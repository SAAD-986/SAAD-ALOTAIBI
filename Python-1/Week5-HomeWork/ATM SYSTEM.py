balance = 1000
while True:
    print("\n--- ATM Menu ---")
    print("1 - Show Balance\n2 - Deposit\n3 - Withdraw\n0 - Exit")
    choice = input("Select an option: ")

    if choice == "0":
        print("Thank you for using the ATM. Goodbye!")
        break
    
    elif choice == "1":
        print(f"Current balance: {balance} SAR")
        
    elif choice in ["2", "3"]:
        
        while True:
            amount = int(input("Choose amount (50, 100, 200, 500) or 0 to cancel: "))
            
            if amount == 0:
                break
            elif amount in [50, 100, 200, 500]:
                if choice == "2":
                    balance += amount
                    print(f"New balance: {balance} SAR")
                else: 
                    if balance >= amount:
                        balance -= amount
                        print(f"New balance: {balance} SAR")
                    else:
                        print("Insufficient funds")
                break
            else:
                print("Invalid amount. Please try again.")
    else:
        print("Invalid option, please try again.")