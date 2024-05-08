class Cliente:
    def __init__ (self, nome, anoNascimento, sexo, saldo, endereco, ativo):
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


    def calculoIdade(self):
       anoAtual = 2024
       idadeCliente = anoAtual - self.anoNascimento
       print("A idade do cliente é:", idadeCliente)

    def verificarSaldo(self):
        if self.saldo > 0:
            print("O saldo é positivo.")
        else:
            print("O saldo é negativo.")
      

objeto1 = Cliente("Guilherme", 1998, "M", 5000, "Rua Teste", True)
objeto2 = Cliente("Ana", 2007, "M", -5000, "Rua Teste", True)
objeto3 = Cliente("Evelyn", 2007, "M", 5000, "Rua Teste", False)
objeto1.imprimir()
objeto2.imprimir()
objeto3.imprimir()

objeto2.calculoIdade()

objeto1.verificarSaldo()
objeto2.verificarSaldo()
objeto3.verificarSaldo()

  
    