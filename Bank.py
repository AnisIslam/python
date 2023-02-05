class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000

    def get_balance(self):
        return self.balance
    def withdraw (self , amount):
        if amount < self.min_withdraw:
            return f"no money for you. Minimum need to take {self.min_withdraw} taka"
        elif amount > self.max_withdraw:
            return f"crosses max limit : {self.max_withdraw}"
        elif amount > self.balance:
            return "No money sorry"
        else:
            self.balance = self.balance -amount
            return f"Here is yuor money : {amount}"
my_bank = Bank(8000)
reply = my_bank.withdraw(1500)
print(reply)