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
            confirmacao = str(input(f"Para a conta de {contas[i][2]}? (S/N) ")).upper()
            if confirmacao == "S":
                valor = float(input("Informe o valor do depósito: "))
                if valor > 0:
                    contas[i][3] += valor
                    contas[i][4].append(f"Depósito: R$ {valor:.2f}")
                    sucesso = f"O Depósito de R$ {valor:.2f} realizado com sucesso!"
                    print("\n", sucesso.center(40), f"\n\tSaldo atualizado: R$ {contas[i][3]:.2f}")
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
    limite = 500.00
    conta_saque = int(input("Informe a conta para o saque: "))
    for i in range(len(contas)):
        if conta_saque == contas[i][1]:
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > float(contas[i][3])
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
                break
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")
                break
            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")
                break
            elif valor > 0:
                contas[i][3] -= valor
                contas[i][4].append(str(f"Saque: R$ {valor:.2f}"))
                numero_saques += 1
                print(f"Saque de {valor} realizado com sucesso!")
                break
    else:
        print("Operação falhou! O valor informado é inválido.")


def exibir_extrato(contas):
    conta = int(input("Qual conta deseja ver o extrato? "))
    for i in contas:
        if conta == i[1]:
            if i[1] == "":
                print("| EXTRATO - Banco Python |".center(80, "="))
                print("Não foram realizadas movimentações.")
            else:
                print("| EXTRATO - Banco Python |".center(80, "="))
                for j in range(len(i[4])):
                    print(i[4][j])
                print("-"*80)
                print(f"Saldo: R$ {i[3]:.2f}")
                print("="*80)


def exibir_usuario(usuario):
    print(f"\nUsuário {usuario[0]} {usuario[1]}".center(200),
          f"\nCPF: {usuario[2][0:4]}".center(200))


def criar_usuario(usuarios):
    nome = str(input("Digite o nome do usuário: ")).title()
    sobrenome = str(input("Digite o sobrenome: ")).title()
    cpf = int(input("CPF: "))
    usuario = nome, sobrenome, cpf
    usuarios.append(usuario)
    print(f"\nUsuário {nome} {sobrenome}".center(200),
          f"\nadicionado com sucesso!".center(200))
    return usuarios


def procurar_usuario(usuarios):
    usuario = str(input("Qual usuário deseja procurar? "))
    usuario = usuario.title()
    for i in usuarios:
        if usuario == i[0]:
            print(i)
            break
    else:
        print("Usuário não encontrado.")


def listar_usuarios(usuarios):
    print("| Lista de Usuários - Banco Python |".center(80, "-"))
    for usuario in usuarios:
        print(f"|\tNome: {usuario[0]} {usuario[1]}".ljust(37, " "), f"| CPF: {usuario[2]} |".rjust(40, " "))
        print("".center(80, "-"))


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
    print("| Lista de Contas - Banco Python |".center(80, "-"))
    for conta in contas:
        print(f"\n| Agência: {conta[0]} | Conta: {conta[1]} - {conta[2]}"
              f"\n| Saldo: {conta[3]:.2f}"
              f"\n| Extrato: ")
        for i in range(len(conta[4])):
            print("\t", conta[4][i])
        print("".center(80, "-"))


def main():
    numero_saques = 0

    usuarios = [["João", "Macedo", 43566785476],
                ["Pedro", "Alcantara", 26743947536],
                ["Ana", "Montenegro", 36538546837],
                ["Maria", "Grutsky", 32239854897],
                ["Marcos", "Strunksky", 26753578934],
                ["Josete", "Oliveira", 24467343974]]

    contas = [["0001", 1, "Pedro", 3045.89, ["Depósito R$ 3045.89"]],
              ["0001", 2, "Ana", 34360.78, ["Depósito R$ 34360.78"]],
              ["0001", 3, "Marcos", 360.78, ["Depósito R$ 360.78"]],
              ["0001", 4, "Josete", 1200.00, ["Depósito R$ 300.00", "Depósito R$ 300.00",
                                              "Depósito R$ 300.00", "Depósito R$ 300.00"]],
              ["0001", 5, "Maria", 4223.85, ["Depósito R$ 4223.85"]]]

    while True:
        opcao = menu()
        if opcao == "d":
            depositar(contas)

        elif opcao == "s":
            sacar(contas, numero_saques)

        elif opcao == "e":
            exibir_extrato(contas)

        elif opcao == "u":
            usuarios = criar_usuario(usuarios)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "pu":
            procurar_usuario(usuarios)

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
