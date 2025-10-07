class SavingsAccount:
    def __init__(self): self.balance = 0
    def deposit(self, amt): self.balance += amt if amt > 0 else 0
    def withdraw(self, amt):
        if 0 < amt <= self.balance: self.balance -= amt
        else: print("Insufficient funds")
    def show(self): print(f"Savings: ${self.balance}")

class CheckingAccount:
    def __init__(self): self.balance = 0; self.od_limit = 100
    def deposit(self, amt): self.balance += amt if amt > 0 else 0
    def withdraw(self, amt):
        if 0 < amt <= self.balance + self.od_limit: self.balance -= amt
        else: print("Overdraft limit exceeded")
    def show(self): print(f"Checking: ${self.balance}")

s, c = SavingsAccount(), CheckingAccount()

while True:
    choice = input("1:DepSav 2:WithSav 3:DepChk 4:WithChk 5:Show 6:Exit > ")
    if choice == '1': s.deposit(float(input("Amt: ")))
    elif choice == '2': s.withdraw(float(input("Amt: ")))
    elif choice == '3': c.deposit(float(input("Amt: ")))
    elif choice == '4': c.withdraw(float(input("Amt: ")))
    elif choice == '5':
        s.show()
        c.show()
    elif choice == '6': break
    else: print("Invalid")
