class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def display_details(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Holder Name: {self.__holder_name}")
        print(f"Balance: {self.__balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.03):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print("Interest applied.")

    def withdraw(self, amount):
        if amount > self.get_balance():
            print("Withdrawal exceeds balance in savings account.")
        else:
            super().withdraw(amount)


class CurrentAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=500.0):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            available_balance = self.get_balance()
            if amount <= available_balance:
                super().withdraw(amount)
            else:
                super().withdraw(available_balance)
                print("Overdraft used.")
        else:
            print("Overdraft limit exceeded.")


def main():
    savings = SavingsAccount("SA001", "Alice", 1000)
    current = CurrentAccount("CA001", "Bob", 500)

    savings.deposit(500)
    savings.withdraw(300)
    savings.apply_interest()
    print("Savings Balance:", savings.get_balance())

    print()

    current.deposit(200)
    current.withdraw(900)
    print("Current Balance:", current.get_balance())


if __name__ == "__main__":
    main()
