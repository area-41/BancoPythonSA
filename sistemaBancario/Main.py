import textwrap

from Agencia import Agencia
from Usuario import Usuario
from Conta import Conta

"""
'Lista de contas Banco Money S.A'
"""
def main():
    #LIMITE_SAQUES = 3
    #AGENCIA = "0001"

    #saldo = 0
    #limite = 500
    #extrato = ""
    #numero_saques = 0

    #usuarios = []
    #contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            Conta.depositar(Conta.saldo, valor, Conta.contas.extrato)


        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = Conta.sacar(
                saldo=Conta.saldo,
                valor=valor,
                extrato=Conta.extrato,
                limite=Conta.limite,
                numero_saques=Conta.numero_saques,
                limite_saques=Conta.LIMITE_SAQUES
            )

        elif opcao == "e":
            Conta.exibir_extrato(Conta.contas.saldo, extrato=Conta.extrato)

        elif opcao == "c":
            Conta.criar_conta()

        elif opcao == "lc":
            Conta.listar_contas()

        elif opcao == "u":
            Usuario.criar_usuario()

        elif opcao == "lu":
            Usuario.listar_usuarios()

        elif opcao == "a":
            Agencia.criar_agencia()

        elif opcao == "la":
            Agencia.listar_agencias()

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Nova Conta
    [lc] Listar Contas
    [u] Novo Usuário
    [lu] Listar Usuários
    [a] Nova Agência
    [a] Listar Agências
    [q] Sair

    => """
    return input(textwrap.dedent(menu))


if __name__ == '__main__':
    main()