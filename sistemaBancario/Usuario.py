class Usuario:

    usuarios = []

    def __init__(self, nome, cpf, codigo, agencia):
        self.nome = nome
        self.cpf = cpf
        self.codigo = codigo
        self.agencia = agencia


    def criar_usuario():
        usuario = Usuario(str(input("Nome: ")), int(input("CPF: ")), len(Usuario.usuarios), int(input("Agência: ")))
        Usuario.usuarios.append(usuario)
        print(f"Cliente {usuario.nome} criado!".center(50))

    def listar_usuarios():
        for usuario in Usuario.usuarios:
            print(f"Usuário: {usuario.codigo} - {usuario.nome} : {usuario.cpf}")

    def filtrar_usuario(cpf, usuarios):
        pass