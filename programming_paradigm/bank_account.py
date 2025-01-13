class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount instance with an optional initial balance.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount to the account balance.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount if funds are sufficient.
        Returns True if successful, False otherwise.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Print the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
