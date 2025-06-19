# Task 1 define class
# Task 2 impliment class
class BankAccount:
    def __init__ (self,account_number,holder_name,initial_balance=0):
        "Initialize a new bank account number, holder's name,and initial balance."
        self.account_number=account_number
        self.holder_name=holder_name
        self.balance=initial_balance

# Task 3 Implement Deposit and Withdraw Methods
    def deposit(self,amount):
        "deposit the specific amount into the account."
        if amount >0:
            self.balance += amount
            print(f"Deposited  {amount:2f}. New balance is  {self.balance:2f}.")
        else:
            print("Deposited amount must be positive.")
    def withdraw(self,amount):
        "withdraw the specific amount from the account."
        if 0<amount <=self.balance:
            self.balance -= amount
            print(f"Withdraw  {amount:2f}. New balance is  {self.balance:2f}.")
        else:
            print("Insufficient funds or invalid amount.")

# Task 4 check the Account Balance
    def get_balance(self):
        "Return the current balance of the account."
        return self.balance
## Task 5 :String Representation of the Account     
    def __str__(self):
        "return a string representation of the acount details."
        return(f"Account Number:{self.account_number}\n"
                f"Holder Name :{self.holder_name}\n"
                f"Balance : {self.balance:.2f}")
if __name__=="__main__":
    account=BankAccount("12345678","Ramar",15000)
    print(account)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)
    #check balance
    print(f"Final balance: {account.get_balance():.2f}")
        