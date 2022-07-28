from models.client import Client
from utils.helper import format_float_for_real_currency

class Account:

    id_account_counter = 2001

    def __int__(self, client):
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

    @property
    def _calc_total_balance(self):
        return self.balance + self.limit

    def deposit(self, value):
        pass

    def withdraw(self, value):
        pass

    def transfer(self, to, value):
        pass