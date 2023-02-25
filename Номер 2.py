class Bank_account :
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance
    def Withdraw(self,a):
        self.balance = self.balance - a
        return self.balance
    def Deposit(self,b):
        self.balance = self.balance + b
        return self.balance
    def Display(self):
        print(f'у {self.name} на аккаунте {self.account_number} осталось {self.S}')

Yara = Bank_account('123','Yara',1034)
Yara.Withdraw(23)
Yara.Deposit(890)
Yara.Display()

