class BankAccount:
	def __init__(self, int_rate, balance):
         self.int_rate=int_rate
         self.balance = balance
	def deposit(self, amount):
		self.balance+=amount
	def withdraw(self, amount):
		if self.balance<amount:
		    print("Insufficient funds: Charging a $5 fe")
		    self.balance-=5
		else:
		    self.balance-=amount
	def display_account_info(self):
		print(f"Balance: $ {self.balance}")
	def yield_interest(self):
		if self.balance>0:
		    self.balance+=self.balance*self.int_rate

    
x=BankAccount(0.05,5000)
y=BankAccount(0.03,1000)
x.deposit(1000)
x.deposit(3000)
x.deposit(500)
x.withdraw(1000)
x.yield_interest()