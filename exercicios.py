class Exercicios:
    def __init__(self, nomeAluno, numeroChamada):
        self.nomeAluno = nomeAluno
        self.numeroChamada = numeroChamada

    def imprimir(self):
        print("Nome do aluno:", self.nomeAluno, "Número chamada:", self.numeroChamada)

    def exercicio1(self):
        nome = "Ana"
        idade = 17
        sexo = "Feminino"
        status = "Solteira"
        print("Meu nome é", nome)
