class Agencia:
    agencias = []

    def __init__(self, agencia, cidade, estado):
        self.agencia = agencia
        self.cidade = cidade
        self.estado = estado


    def criar_agencia():
        agencia = input("Agência: ")
        Agencia.agencias.append(Agencia(agencia, cidade=input("Cidade: "), estado=input("Estado: ")))
        print(f'Agência {agencia} criada com sucesso!'.center(50))

    def listar_agencias():
        for agencia in Agencia.agencias:
            print(f"{agencia.agencia} - {agencia.cidade}/{agencia.estado}")
