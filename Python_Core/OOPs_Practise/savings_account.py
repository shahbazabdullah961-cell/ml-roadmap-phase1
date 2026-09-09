class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance  

    def deposit(self, deposit_amount: float):
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"Deposited: ${deposit_amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, withdraw_amount: float):
        
        if 0 < withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f"Successfully withdrew: ${withdraw_amount:.2f}")
        else:
            print("Error: Insufficient funds or invalid amount.")

    def display(self):
        print(f"Name: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate  # Works now because self.balance exists
        self.deposit(interest)


bank = SavingsAccount("ALI", 23.0)
bank.add_interest()  
bank.withdraw(10.0)  
bank.display()

        