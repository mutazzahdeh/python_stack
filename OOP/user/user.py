class user():
    def __init__(self,name,email,balnce):
        self.email=email
        self.name=name
        self.balnce=balnce
    def make_withdrawal(self,amount):
        self.balnce-=amount
        return self.balnce
    def display_user_balance(self):
        print(f"user:{self.name}, Balance:${self.balnce}")
    def transfer_money(self, other_user, amount):
         self.balance-=amount
         self.other_user.balance=amount
y=user(name="mohmad",email="asdsa",balnce=1000)


print(y.name)
print(y.make_withdrawal(3000))




    
    
    
