class BankAccount:
    bank_name="FiBank"
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if (self.balance - amount) < 0 :
            print ("Insufficient funds: Charging a $5 fee")
            self.balance-=5
            return self
        else:
            self.balance -= amount
            return self

    def yield_interest(self):
        if self.balance  <= 0 :
            return self
        else :
            self.balance += (self.balance * self.int_rate)
            return self
            
    @classmethod
    def display_account_info(cls):
        for account in cls.accounts:
            print("Balance of " + account.accountHolder +" : " +  str(account.balance))