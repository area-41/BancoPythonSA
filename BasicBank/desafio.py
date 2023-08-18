import textwrap


def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Nova Conta
    [l] Listar Contas
    [u] Novo Usuário
    [lu] Listar Usuários
    [pu] Procurar Usuário
    [q] Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(contas):
    conta_deposito = int(input("Informe a conta para o depósito: "))
    for i in range(len(contas)):
        if conta_deposito == contas[i][1]:
            confirmacao = str(input(f"Para a conta de {contas[i][2]}? (S/N)")).upper()
            if confirmacao == "S":
                valor = float(input("Informe o valor do depósito: "))
                if valor > 0:
                    contas[i][3] += valor
                    contas[i][4].append(f"Depósito: R$ {valor:.2f}")
                    sucesso = f"O Depósito de R$ {valor:.2f} realizado com sucesso!"
                    print("\n", sucesso.center(40),f"\n\tSaldo atualizado: R$ {contas[i][3]}")
                    break
                else:
                    print("Operação falhou! O valor informado é inválido.")
                    break
            elif confirmacao == "N":
                print("Depósito cancelado.")
                break
    else:
        print("Conta não encontrada.")



def sacar(contas, numero_saques):
    limite = 500
    conta_saque = int(input("Informe a conta para o saque: "))
    for i in range(len(contas)):
        if conta_saque == contas[i][1]:
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > contas[i][1]
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
            elif valor > 0:
                contas[i][3] -= valor
                contas[i][4] += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                return numero_saques, contas
            # elif valor > 0:
            #     saldo -= valor
            #     extrato += f"Saque: R$ {valor:.2f}\n"
            #     numero_saques += 1
            #     return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    nome = str(input("Digite o nome do usuário: ")).title()
    sobrenome = str(input("Digite o sobrenome: ")).title()
    cpf = int(input("CPF: "))
    usuario = nome, sobrenome, cpf
    usuarios.append(usuario)
    print(f"\nUsuário {nome} {sobrenome}".center(200),
          f"\nadicionado com sucesso!".center(200))
    return usuarios


def filtrar_usuario(usuarios):
    usuario = str(input("Qual usuário deseja procurar?"))
    usuario = usuario.title()
    for i in usuarios:
        if i == usuario[0]:
            print(i)
        else:
            print("Usuário não encontrado.")


def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Usuário: {usuario[0]} {usuario[1]} - CPF: {usuario[2]}")


def criar_conta(usuarios, contas):
    AGENCIA = "0001"
    numero_conta = len(contas)+1
    usuario = str(input("Qual usuário quer adicionar à conta? "))
    usuario = usuario.title()
    for i in range(0, len(usuarios)):
        # print(usuarios[i][0])
        if usuario == usuarios[i][0]:
            for j in range(0, len(contas)):
                # print(j)
                # print(contas[j][2])
                if usuario == contas[j][2]:
                    print(f"Já existe uma conta com este usuário\n Conta:{contas[i-1][1]}")
                    break
            else:
                saldo = 0
                extrato = []
                conta = [AGENCIA, numero_conta, usuario, saldo, extrato]
                contas.append(conta)
                print(f"\nConta com {usuario} criada com sucesso."
                      f"\nNúmero da conta: {numero_conta}"
                      f"\nAgência: {AGENCIA}")
                break
            break
    else:
        print("Usuário não encontrado.")



def listar_contas(contas):
    print("---| Lista de Contas - Banco Python |---".center(50))
    for conta in contas:
        print(f"\nAgência: {conta[0]} | Conta: {conta[1]} - {conta[2]}"
              f"\nSaldo: {conta[3]}"
              f"\nExtrato: {conta[4]}\n")


def main():
    # saldo = 0
    limite = 500
    # extrato = ""
    numero_saques = 0

    usuarios = [["João", "Macedo", 43566785476], ["Pedro", "Alcantara", 26743947536], ["Ana", "Montenegro", 36538546837]]
    contas = [["0001", 1, "Pedro", 3045.89, ["Depósito R$ 3045.89"]],
              ["0001", 2, "Ana", 34360.78, ["Depósito R$ 34360.78"]]]

    while True:
        opcao = menu()
        if opcao == "d":
            depositar(contas)

        elif opcao == "s":
            numero_saques, contas = sacar(contas, numero_saques)

            # valor = float(input("Informe o valor do saque: "))
            # excedeu_saldo = valor > saldo
            # excedeu_limite = valor > limite
            # excedeu_saques = numero_saques >= LIMITE_SAQUES
            #
            # if excedeu_saldo:
            #     print("A operação falhou, saldo insuficiente.")
            # if excedeu_limite:
            #     print("A operação falhou, valor saque excede o limite.")
            # if excedeu_saques:
            #     print("A operação falhou, atingiu o limite de saques.")
            # elif valor > 0:
            #     saldo -= valor
            #     extrato += f"Saque: R$ {valor:.2f}\n"
            #     numero_saques += 1
            # else:
            #     print("Operação falhou, valor inválido.")

        elif opcao == "e":
            exibir_extrato(contas)

        elif opcao == "u":
            usuarios = criar_usuario(usuarios)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "pu":
            filtrar_usuario(usuarios)

        elif opcao == "c":
            criar_conta(usuarios, contas)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    LIMITE_SAQUES = 3
    main()
