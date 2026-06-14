class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} SAR. New balance: {self.balance} SAR")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} SAR. New balance: {self.balance} SAR")
        else:
            print("Insufficient funds!")

    def show(self):
        print(f"{self.owner} has {self.balance} SAR")

a = BankAccount("Sara", 1000)

a.deposit(500)
a.withdraw(300)
a.show()