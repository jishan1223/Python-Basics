class BankAccount:
    
    def __init__(self,name):
        self.name = name
        self.balance = 0.0
            
    def showBalance(self):
        print(f"{self.name}, new balance is {self.balance}")
        
    def depositMoney(self, amount):
        self.balance += amount
        print(f"{self.name}, new balance is {self.balance}")
        
    def withdrawMoney(self, amount):
        if amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"{self.name}, new balance is {self.balance}")
            
            
olivia = BankAccount("olivia")
olivia.showBalance()
olivia.depositMoney(1000)
print(olivia.balance)
olivia.withdrawMoney(500)
        