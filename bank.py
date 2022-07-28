from typing import List
from time import sleep

from models.client import Client
from models.account import Account

accounts = []

def main():
    menu()

def menu():
    print("===============================================")
    print("====================ATM========================")
    print("====================BANK=======================")
    print("===============================================")
    print("===============================================")

    print("Select an option below: ")
    print("1 - Open an account")
    print("2 - Withdraw")
    print("3 - Deposit")
    print("4 - Transfer")
    print("5 - List accounts")
    print("6 - Exit")

    opcao = int(input("Option: "))

    if opcao == 1:
        create_account()
    elif opcao == 2:
        withdraw()
    elif opcao == 3:
        deposit()
    elif opcao == 4:
        trasnfer()
    elif opcao == 5:
        list_accounts()
    elif opcao == 6:
        print("See you later!")
        sleep(2)
        exit(0)
    else:
        print("Invalid option")

def create_account():
    print('Enter client data:')
    name = input("Client name: ")
    email = input("Client email: ")
    document = input("Client document: ")
    date_of_birth = input("Client birth date: ")

    client = Client(name, email, document, date_of_birth)
    account = Account(client)

    accounts.append(account)

    print('Account created susccessfully')
    print('Account info:')
    sleep(2)
    print(account)
    menu()

def withdraw():
    pass

def deposit():
    pass

def trasnfer():
    pass

def list_accounts():
    pass

def search_account_by_id(id_account):
    pass

if __name__ == '__main__':
    main()