class BankAccount:
    #initializer/constructor
    def __init__(self, account_holder: str, account_balance: float = 0):
        #Attributes
        self.account_holder = account_holder #public
        self.__account_balance = account_balance if account_balance >= 0 else 0 # private

    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__account_balance += amount
        return self.__account_balance

    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.__account_balance:
            raise Exception("Insufficient funds!")
        self.__account_balance -= amount
        return self.__account_balance

    
    def get_balance(self):
        return self.__account_balance
    
    def get_account_holder(self):
        return self.account_holder
    
    
    
