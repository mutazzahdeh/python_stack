from BankAccount import BankAccount

class user:
    def __init__(self,name, year_of_birth):
        self.name=name
        self.year_of_birth=year_of_birth
        self.account=BankAccount()
    def make_withdrawal(self,amount):
            return self.account.withdrawal(amount)
 
    def display_user_balance(self):
        print(f"user:{self.name}, Balance is:$",end=" ")
        self.account.display_account_info
    def deposite(self,amount):
        self.account.deposit(amount)
    def transfer_money(self, other_user, amount):
        if self.make_withdrawal(amount):
            other_user.deposit(amount)
            return True

        return False

