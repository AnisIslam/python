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
    def deposit(self, amount):
        self.balance = self.balance + amount
print('Input the bank balance currently you have')
balance = int(input())
my_bank = Bank(balance)
print('Input your withdraw amount')
withdrawAmount = int(input())
reply = my_bank.withdraw(withdrawAmount)
print(reply)
print(my_bank.get_balance())

print('Input your deposit amount')
depositAmount = int(input())
my_bank.deposit(depositAmount)
print(my_bank.get_balance())