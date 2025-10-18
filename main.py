
# main.py
from bankAccount import BankAccount


account1 = BankAccount("Abrar", 500)

print(f"Account holder: {account1.get_account_holder()}")
print(f"Initial balance: {account1.get_balance()}")
print()

try:
    account1.deposit(300)
    print(f"Balance after deposit: {account1.get_balance()}")
except ValueError as e:
    print("Error:", e)

try:
    account1.withdraw(200)
    print(f"Balance after withdrawal: {account1.get_balance()}")
except Exception as e:
    print("Error:", e)

