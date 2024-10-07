class BankAccount:
    """
    A simple BankAccount class.
    """

    def __init__(self, initial_balance=0):
        """
        Initialize account balance.

        Args:
            initial_balance (float, optional): Initial balance. Defaults to 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit amount into account.

        Args:
            amount (float): Amount to deposit.
        """
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw amount from account if sufficient funds.

        Args:
            amount (float): Amount to withdraw.

        Returns:
            bool: True if withdrawal successful, False otherwise.
        """
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """
        Print current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")


