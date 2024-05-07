class Cliente:
    def __init__ (nome, anoNascimento, sexo, saldo, endereco, ativo):
        self.nome = nome
        self.anoNascimento = anoNascimento
        self.sexo = sexo
        self.saldo = saldo
        self.endereco = endereco
        self.ativo = ativo

    def imprimir(self):
        print("Nome:", self.nome)
        print("Ano de Nascimento:", self.anoNascimento)
        print("Sexo:", self.sexo)
        print("Saldo:", self.saldo)
        print("Endereço:", self.endereco)
        print("Ativo:", self.ativo)

    def ValidarCliente(self):
        if self.ativo:
            print("O cliente", self.nome, "esta ativo")
        else:
            print("O cliente", self.nome, "Inativo")

objeto1 = Cliente("Guilherme", 1998, "M", 5000, "Rua Teste", True)
objeto2 = Cliente("Ana", 1998, "M", -5000, "Rua Teste", True)
objeto3 = Cliente("Evelyn", 1998, "M", 5000, "Rua Teste", False)
objeto1.imprimir()
objeto2.imprimir()
objeto3.imprimir()

