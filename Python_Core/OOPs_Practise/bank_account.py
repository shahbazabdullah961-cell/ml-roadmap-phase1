class BankAccount:
    def __init__(self,account_holder,initial_balance=0.0):
        self.account_holder= account_holder
        self.self_balance=initial_balance
    def deposit(self,deposit_amount: float):
        if deposit_amount > 0:
            self.self_balance+=deposit_amount
        else:
            print("Error while deposit")
    def withdraw(self,withdraw_amount:float):
        if withdraw_amount < self.self_balance :
            self.self_balance-=withdraw_amount
            print("Operation successful")
        else:
            print("Error in Withdraw")
    def display(self):
        print("Name:",self.account_holder)
        print("Balance:",self.self_balance)
    
    
    
bank=BankAccount("ALI",23)
bank.deposit(400)
bank.withdraw(422)
bank.display()


        