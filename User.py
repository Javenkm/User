class User:
    def __init__(self, name, email):
        self.name = name 
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def display_user_balance(self):
        print(f"Name: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, amount, other_user):
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount
        print(f"{self.name} just transferred {amount} dollars to {other_user.name}")

Javen = User ("Javen", "Javenkm@gmail.com")
Israel = User ("Alpha", "alphaDog@gmail.com")
Ella = User ("Beta", "betasucks@gmail.com")

Javen.make_deposit(5000)
Javen.make_deposit(1500)
Javen.make_deposit(250)
Javen.make_deposit(-120)
Javen.display_user_balance()
Israel.make_deposit(900)
Israel.make_deposit(100)
Israel.make_deposit(-50)
Israel.make_deposit(-50)
Israel.display_user_balance()
Ella.make_deposit(1225)
Ella.make_deposit(-100)
Ella.make_deposit(-50)
Ella.make_deposit(-100)
Ella.display_user_balance()

Javen.display_user_balance()
Javen.transfer_money(250, Ella)
Javen.display_user_balance()
Israel.display_user_balance()
Ella.display_user_balance()