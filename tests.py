from models.client import Client
from models.account import Account

filipe = Client('Filipe Vasconcelos', 'filipev@me.com', '323.323.232-2', '03/17/1999')
mariana = Client('Mariana Toledo', 'marianatoledo@me.com', '123.123.123-22', '1/1/2002')

print(filipe)
print(mariana)

contaf = Account(filipe)
contam = Account(mariana)
print('----------------------------------')
print('----------------------------------')
print(contaf)
print('----------------------------------')

print(contam)