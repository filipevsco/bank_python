from datetime import date
from utils.helper import date_for_str, str_for_date


class Client:
    counter = 1001

    def __init__(self, name, email, document, date_of_birth):
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

    @property
    def document(self):
        return self.__document

    @property
    def date_of_birth(self):
        return date_for_str(self.__date_of_birth)

    @property
    def registration_date(self):
        return date_for_str(self.__registration_date)

    def __str__(self):
        return f'Id: {self.id}\nNome: {self.name}\nemail: {self.email}\nDate of Birth: {self.date_of_birth}\n' \
                f'Registration Date: {self.registration_date}'