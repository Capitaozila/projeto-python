class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco_interno(self, rua, numero):
        # self.enderecos.append(Endereco(rua, numero))
        endereco = Endereco(rua, numero)
        self.enderecos.append(endereco)

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente("Maria")
cliente1.inserir_endereco("Dunas Mar", 333)
cliente1.inserir_endereco("Rua B", 3813)
cliente1.listar_enderecos()

del cliente1

print('Aqui termina meu código')
