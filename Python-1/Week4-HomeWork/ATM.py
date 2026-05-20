Balance=6
print("1-Check balance")
print("2-Deposit 100 SAR")
print("3-Check balance")
print("4-Withdraw 50 SAR")
choice = input("Enter your choice (1-4): ")

match choice:
    case "1":
        print(f"Current balance: {Balance} SAR")
    case "2":
        Balance += 100 
        print(f"New balance{Balance} SAR")
       
        
    case "3":
 
        if Balance < 50:
            print("Insufficient funds")
        else:
            Balance -= 50 
            print(f"New balance: {Balance} SAR")
            
    case "4":
        print("Goodbye!")
        
    case _:
        
        print("Invalid choice")  