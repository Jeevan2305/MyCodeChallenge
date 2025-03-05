# Create a class for a bank account with methods for deposit and withdrawal.
class BankAccount:
    def __init__(self, name, initial_balance = 0):
        self.name = name
        self.balance = initial_balance
        self.transactions = []
        
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(amount)
 
    def withdrawal(self, amount):
        if self.balance < amount:
            print("Transactions failed. Try again")
        else:
            self.balance -= amount
            self.transactions.append((amount * -1))

    def checkStatement(self):
        print(f"{self.name}'s Bank Balance : {self.balance}")
        print(f"{self.name}'s Transaction : {self.transactions}")

Person1 = BankAccount("Ram")
Person2 = BankAccount("Shalani", 2000)

Person1.deposit(1000)
Person1.withdrawal(300)
Person1.checkStatement()

Person2.withdrawal(2500)
Person2.deposit(300)
Person2.deposit(500)
Person2.checkStatement()
