from datetime import date
from utils.helper import date_for_str, str_for_date


class Client:
    counter = 1

    def __int__(self, name, email, document, date_of_birth):
        self.__id = Client.counter
        self.__name = name
        self.__email = email
        self.__document = document
        self.__date_of_birth = str_for_date(date_of_birth)
        self.__registration_date = date.today()
        Client.counter += 1

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

