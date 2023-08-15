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
    [q] Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        sucesso = f"O Depósito de R$ {valor:.2f} realizado com sucesso!"
        print("\n", sucesso.center(40))
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(saldo, valor, extrato, limite, numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    nome = str(input("Digite o nome do usuário: "))
    sobrenome = str(input("Digite o sobrenome: "))
    cpf = int(input("CPF: "))
    usuario = nome, sobrenome, cpf
    usuarios.append(usuario)
    print(f"\nUsuário {nome} {sobrenome}".center(200),
          f"\nadicionado com sucesso!".center(200))
    return usuarios


def filtrar_usuario(usuarios):
    usuario = str(input("Qual usuário deseja procurar?"))
    for i in usuarios:
        if i == usuario[0]:
            print(i)
        else:
            print("Usuário não encontrado.")

def listar_usuarios(usuarios):
    for usuario in usuarios:
        print(f"Usuário: {usuario[0].upper()} {usuario[1].upper()} - CPF: {usuario[2]}")


def criar_conta(agencia, numero_conta, usuarios):
    usuario = str(input("Qual usuário quer adicionar à conta? "))
    saldo = 0
    for i in range(len(usuarios)):
        if usuario == usuarios[i][0]:
           conta = agencia, numero_conta, usuario, saldo
           print(f"\nConta com {usuario} criada com sucesso."
                 f"\nNúmero da conta: {numero_conta}"
                 f"\nAgência: {agencia}")
           return conta
        else:
            print("Usuário não encontrado.")


def listar_contas(contas):
    print("---| Lista de Contas - Banco Python |---".center(50))
    for conta in contas:
        print(f"Agência: {conta[0]} | Conta: {conta[1]} - {conta[2].upper()} Saldo: {conta[3]}")


def main():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    usuarios = [("Pedro", "Alcantara", 26743947536), ("Ana", "Montenegro", 36538546837)]
    contas = [("0001", 2, "Pedro", 3045.89), ("0001", 3, "Ana", 34360.78)]

    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(valor, saldo, extrato)

            # try:
            #     valor = float(input("Informe o valor do depósito: "))
            #     if valor is float:
            #         saldo, extrato = depositar(valor, saldo, extrato)
            # except:
            #     print("Valor inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo, valor, extrato, limite, numero_saques)

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
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            usuarios = criar_usuario(usuarios)

        elif opcao == "lu":
            listar_usuarios(usuarios)

        elif opcao == "c":
            contas.append(criar_conta(agencia=AGENCIA, numero_conta=len(contas), usuarios=usuarios))

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    LIMITE_SAQUES = 3
    main()
