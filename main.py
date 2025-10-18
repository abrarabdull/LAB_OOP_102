# main.py
from bankAccount import BankAccount


account1 = BankAccount("Abrar", 500)

while True:
    print("\n Welcome to Bank System")
    print("1 Deposit money")
    print("2 Withdraw money")
    print("3 Check balance")
    print("4 Show account holder")
    print("5 Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        try:
            amount = float(input("Enter amount to deposit: "))
            account1.deposit(amount)
        except ValueError as e:
            print("Error:", e)
        input("\n Press Enter to continue...")

    elif choice == "2":
        try:
            amount = float(input("Enter amount to withdraw: "))
            account1.withdraw(amount)
        except Exception as e:
            print("Error:", e)
        input("\n Press Enter to continue...")

    elif choice == "3":
        print(f"Current balance: {account1.get_balance()} SAR")
        input("\n Press Enter to continue...")

    elif choice == "4":
        print(f"Account holder: {account1.get_account_holder()}")
        input("\n Press Enter to continue...")

    elif choice == "5":
        print("Thank you for using This Bank System!")
        break

    else:
        print("Invalid choice, please select a valid option.")


