balance = 1000
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited {amount}. New balance: {balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"Withdrew {amount}. New balance: {balance}")

def check_balance():
    print(f"Current balance: {balance}")
while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        amt = int(input("Enter amount to deposit: "))
        deposit(amt)
    elif choice == "2":
        amt = int(input("Enter amount to withdraw: "))
        withdraw(amt)
    elif choice == "3":
        check_balance()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
'''--- Bank Menu ---
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
Enter choice: 1
Enter amount to deposit: 1000
Deposited 1000. New balance: 2000'''
