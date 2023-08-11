class Conta:
    LIMITE_SAQUES = 3
    contas = []

    # saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    # def __init__(self, conta, cliente, agencia):
    def __init__(self, conta):
        self._conta = conta
        # self._saldo = saldo
        self._saldo = 0.0
        # self._cliente = cliente
        # self._agencia = agencia


    def saldo(self):
        return self._saldo


    def criar_conta():
        conta = len(Conta.contas)
        Conta.contas.append(Conta(conta))
        print(f'Conta {conta} criada!'.center(30))

    def listar_contas():
        for conta in Conta.contas:
            print(f"Conta: {conta._conta} - Saldo: {conta._saldo}")

        # for i in range(len(Conta.contas)):
        #     print(f'Conta {i}:', Conta.saldo())



    # def depositar(self, valor, extrato, /):
    def depositar(self, valor):
        self._saldo += valor
        if valor >= 0:
            Conta.saldo += valor
            Conta.extrato += f"Depósito: R$ {valor:.2f}\n"
            sucesso = "O Depósito realizado com sucesso!"
            print("\n", sucesso.center(70))
        else:
            print("Operação falhou! O valor informado é inválido.")

        return Conta.saldo, Conta.extrato

    def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= Conta.LIMITE_SAQUES

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

        else:
            print("Operação falhou! O valor informado é inválido.")

    def exibir_extrato(saldo, /, *, extrato):
        if extrato == 0:
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print("==========================================")
        else:
            print("\n================ EXTRATO ================")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

    def to_String(self):
        print(Conta.contas.__str__())