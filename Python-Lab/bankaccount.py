class BankAccount:
    def __init__(self, accno, name, acctype, balance):
        self.accno = accno
        self.name = name
        self.acctype = acctype
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("\nAccount No:", self.accno)
        print("Name:", self.name)
        print("Account Type:", self.acctype)
        print("Balance:", self.balance)

a = int(input("Enter Account Number: "))
n = input("Enter Name: ")
t = input("Enter Account Type: ")
b = float(input("Enter Initial Balance: "))

acc = BankAccount(a, n, t, b)

acc.deposit(float(input("Enter amount to deposit: ")))
acc.withdraw(float(input("Enter amount to withdraw: ")))
acc.display()
