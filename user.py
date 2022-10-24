from tkinter import E
from bankaccount import BankAccount

class User:
    def __init__(self, name):
        self.name=name
        self.account = {
            "checking": BankAccount (0.2,1400 ),
            "savings": BankAccount (0.5 , 500 ),
        }

    def print_balance(self):
        print(f"{self.name} Savings Balance is :{self.account['savings'].balance} $")
        print(f"            Checking Balance is :{self.account['checking'].balance} $")

    def transfert(self , user2 , amount):
        self.account['checking'].withdraw(amount)
        user2.account['checking'].deposit(amount)

romario = User('Romario Reka')
endi = User('Endi Mimini')
romario.print_balance()
romario.transfert(endi , 500)
romario.print_balance()
endi.print_balance()