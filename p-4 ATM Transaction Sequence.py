# ATM Transaction Sequence Simulation

balance = float(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))

transactions = []
deposits = 0
withdrawals = 0
rejected = 0

withdrawal_limit = 10000

for i in range(n):
    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdraw")

    choice = input("Enter your choice: ")
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount! Transaction rejected.")
        rejected += 1

    elif choice == "1":
        balance += amount
        deposits += amount
        transactions.append(["Deposit", amount, "Successful"])
        print("Deposit successful.")

    elif choice == "2":
        if amount > withdrawal_limit:
            print("Withdrawal limit exceeded!")
            rejected += 1
            transactions.append(["Withdrawal", amount, "Rejected"])

        elif amount > balance:
            print("Insufficient balance!")
            rejected += 1
            transactions.append(["Withdrawal", amount, "Rejected"])

        else:
            balance -= amount
            withdrawals += amount
            transactions.append(["Withdrawal", amount, "Successful"])
            print("Withdrawal successful.")

    else:
        print("Invalid transaction choice!")
        rejected += 1
        transactions.append(["Invalid", amount, "Rejected"])

# Display transaction summary
print("\n========== ATM TRANSACTION SUMMARY ==========")
print("Transaction\tAmount\tStatus")

for t in transactions:
    print(t[0], "\t", t[1], "\t", t[2])

print("\nTotal Deposits: Rs.", round(deposits, 2))
print("Total Withdrawals: Rs.", round(withdrawals, 2))
print("Rejected Transactions:", rejected)
print("Final Balance: Rs.", round(balance, 2))
print("=============================================")