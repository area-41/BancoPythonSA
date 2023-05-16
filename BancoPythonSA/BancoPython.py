class Cliente:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

    def imprime(self):
        print("Cliente: ", self._nome,
              '\nEndereco: ', self._endereco)


class ClientePF(Cliente):
    def __init__(self, nome, endereco, cpf, nascimento):
        super().__init__(nome, endereco)
        self._cpf = cpf
        self._nascimento = nascimento

    def imprime(self):
        print("Cliente: ", self._nome,
              '\nEndereco: ', self._endereco,
              '\nCPF: ', self._cpf,
              '\nNascimento: ', self._nascimento)


class ClientePJ(Cliente):
    def __init__(self, nome, endereco, cnpj):
        super().__init__(nome, endereco)
        self._cnpj = cnpj

    def imprime(self):
        print("Cliente: ", self._nome,
              '\nEndereco: ', self._endereco,
              '\nCNPJ: ', self._cnpj)


class Conta:
    _quant = 0

    @classmethod
    def adiciona_conta(cls):
        cls._quant += 1

    @classmethod
    def quantidade(cls):
        return cls._quant

    def __init__(self, numero, cliente):
        self.adiciona_conta()
        self._numero = numero
        self._saldo = 0.0
        self._cliente = cliente

    def depositar(self, valor):
        self._saldo += valor

    def saldo(self):
        return self._saldo

    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        return False

    def imprime(self):
        print("Conta: ", str(self._numero),
              "\nSaldo: ", str(self._saldo))
        self._cliente.imprime()


class ContaInvestimento(Conta):
    def depositar(self, valor):
        self._saldo += valor * 1.01
