class user():
    def __init__(self,name,email,balnce):
        self.email=email
        self.name=name
        self.balnce=balnce
    def make_withdrawal(self,amount):
        if self.balnce==0:
            return "false"
        elif self.balnce<amount:
            return "false"
        self.balnce-=amount
        return self.balnce
    def display_user_balance(self):
        print(f"user:{self.name}, Balance:${self.balnce}")
    def transfer_money(self, other_user, amount):
         self.balnce-=amount
         self.other_user.balnce+=amount
y=user(name="mohmad",email="asdsa",balnce=1000)
x=user(name="ahmad",email="sadas",balnce=3000)

print(y.name)

print(y.make_withdrawal(3000))
y.display_user_balance()
y.transfer_money(x,2000)
 





    
    
    
