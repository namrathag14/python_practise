# interest.py

from datetime import datetime
from bankaccount import BankAccount

class InterestAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate
        self.transaction_log = []

    def deposit(self, amount):
        super().deposit(amount)
        self._log_transaction("Deposit", amount)

    def withdraw(self, amount):
        prev_balance = self.balance
        super().withdraw(amount)
        if self.balance != prev_balance:
            self._log_transaction("Withdraw", amount)

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction("Interest", interest)
        print(f"Interest of ${interest:.2f} applied. New balance: ${self.balance:.2f}")

    def _log_transaction(self, type, amount):
        self.transaction_log.append({
            "type": type,
            "amount": amount,
            "timestamp": datetime.now().isoformat()
        })

    def print_log(self):
        print(f"\nTransaction log for {self.account_holder}:")
        for entry in self.transaction_log:
            print(f"{entry['timestamp']} - {entry['type']}: ${entry['amount']:.2f}")



# test

from intrest import InterestAccount
from car import Car

def test_interest_account():
    acc = InterestAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    acc.apply_interest()
    acc.print_log()

def test_car():
    car = Car("Toyota", "Camry")
    print(f"My car is: {car}")

if __name__ == "__main__":
    test_car()
    test_interest_account()
