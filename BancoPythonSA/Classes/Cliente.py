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
