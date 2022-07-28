from models.client import Client
from utils.helper import format_float_for_real_currency


class Account:

    id_account_counter = 2001

    def __init__(self, client):
        self.__id_account = Account.id_account_counter
        self.__client = client
        self.__balance = 0.0
        self.__limit = 100.0
        self.__total_balance = self._calc_total_balance

        Account.id_account_counter += 1

    def __str__(self):
        return f'Account Number: {self.id_account}\nClient: {self.client.name}\n' \
        f'Total Balance: {format_float_for_real_currency(self.__total_balance)}'

    @property
    def id_account(self):
        return self.__id_account

    @property
    def client(self):
        return self.__client

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value

    @property
    def total_balance(self):
        return self.__total_balance

    @total_balance.setter
    def total_balance(self, value):
        self.__total_balance = value

    @property
    def _calc_total_balance(self):
        return self.balance + self.limit

    def deposit(self, value):
        if value:
            self.balance = self.balance + value
            self.total_balance = self._calc_total_balance
            print("Deposit is done")
        else:
            print("Error")

    def withdraw(self, value):
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calc_total_balance
            else:
                over = self.balance - value
                self.limit = self.limit + over
                self.balance = 0
                self.total_balance = self._calc_total_balance
                print("Withdraw is done!")
        else:
            print("Withdraw error. Try again")

    def transfer(self, to, value):
        if value > 0 and self.total_balance >= value:
            if self.balance >= value:
                self.balance = self.balance - value
                self.total_balance = self._calc_total_balance
                to.balance = to.balance + value
                to.total_balance = to._calc_total_balance
            else:
                over = self.balance - value
                self.balance = 0
                self.limit = self.limit + over
                self.total_balance = self._calc_total_balance
                to.balance = to.balance + value
                to.total_balance = to._calc_total_balance
        else:
            print("Transfer error. Try again")