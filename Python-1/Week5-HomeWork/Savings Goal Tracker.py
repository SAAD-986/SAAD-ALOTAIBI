goal = 400
balance = 0
weekly_deposits = [100, 150, 200, 300]
week = 0
i = 0   
while balance < goal:
    deposit = weekly_deposits[i]
    balance += deposit
    week += 1
    print(f"Week {week}: deposited {deposit}, balance {balance}")
    i += 1
print(f"Goal of {goal} reached in {week} weeks!")