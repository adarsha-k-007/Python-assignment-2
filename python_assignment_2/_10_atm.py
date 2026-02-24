print("===========================")
print("------- ATM SIMULATOR ------")
print("===========================")

# Initial balance
balance = 10000
# Function to check balance
def check_balance(balance):
    print("Current Balance: ₹", balance)
    return balance

# Function to deposit money
def deposit_money(balance):
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance = balance + amount
        print("Deposit successful!")
        print("Updated Balance: ₹", balance)
    else:
        print("Invalid deposit amount!")

    return balance


# Function to withdraw money
def withdraw_money(balance):
    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Invalid withdrawal amount!")

    elif amount > balance:
        print("Insufficient balance!")

    elif balance - amount < 500:
        print("Minimum balance of ₹500 must remain!")

    else:
        balance = balance - amount
        print("Withdrawal successful!")
        print("Updated Balance: ₹", balance)

    return balance

# Menu
while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        balance = check_balance(balance)

    elif choice == 2:
        balance = deposit_money(balance)

    elif choice == 3:
        balance = withdraw_money(balance)

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice! Please select 1-4.")