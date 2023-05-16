from Classes.Conta import *
from Classes.Cliente import *

if __name__ == '__main__':
    cliente01 = ClientePF('Joao Aparecido Alves', 'Rua da Casa Amarela', '24.432.434-34', '1966-01-06')
    print('\nCliente 01\n')
    cliente01.imprime()

    cliente02 = ClientePJ('Casa Japao', 'Rua do Japao', '234.434.434/0001-34')
    print('\nCliente 02\n')
    cliente02.imprime()