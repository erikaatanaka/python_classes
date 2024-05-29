class exercicio:
    def __init__(self):
        print('')

    def ex1(self):
        nomeFuncio = "Érika"
        idade = 17
        salario = 5000
        cargo = "gerente"
        turno = "matutino"
        setor = "rh"
        print("Funcionário:", nomeFuncio)
        print("Idade:" , idade)
        print("Salário:" , salario)
        print("Cargo:" , cargo)
        print("Turno" , turno)
        print("Setor:" , setor)

    
    def ex2(self):
        nomeEscola = "CCM"
        estado = "Paraná"
        numProf = 50
        cidade = "Cdo"
        numMil = 4
        logradouro = "Rua Santos Drumond"
        endNum = 364
        numAlun = 700 
        colegioMili = True
        disciplinas = ["Port", "Mat", "Ingl", "Quim"]
        print("O nome da escola é:", nomeEscola)
        print("Se localiza no estado do" , estado)
        print("Tem" , numProf , "professores")
        print("Na cidade de" , cidade)
        print("Militares: " , numMil)
        print("logradouro:" , logradouro)
        print("Número do endereço:", endNum)
        print("Número de alunos:" , numAlun)
        print ("O colégio é militar?", colegioMili)
        print("Algumas disciplinas são:" , disciplinas)
        

    def ex3(self):
        valor1 = 10
        valor2 = 5
        valor3 = "2"
        valor4 = 8
        valor5 = -5
        soma1 = valor1 + valor2
        soma2 = valor1 + valor2 + valor4
        soma3 = valor1 + valor2 - valor5
        soma4 = valor1 + int(valor3)
        soma5 = valor1 + valor2 
        soma6 = (valor4 + valor2) / 2
        soma7 = (valor1 + valor2 + valor4 + valor5) / 4
        print("A soma do valo1 + valor2 é:", soma1)
        print("A soma do valor1 + valor2 + valor4 é:" , soma2)
        print("A soma do valor1 + valor2 - valor5 é:", soma3)
        print("A soma do valor1 + valor3 é:" , soma4)
        print("O valor1 x valor2 é: " , soma5)
        print("O valor4 x valor2 dividiso por 2 é:" , soma6)
        print("A soma do valor1 + valor2 + valor4 + valor5 dividido por 4 é:", soma7)


    def ex4(self):
        v1 = 2
        v2 = 3
        v3 = 5
        v4 = 6
        soma = v1 + v2 + v3 +v4
        media = soma / 4
        print("A soma dos valores é:", soma)
        print("A média dos valores é:", media)


    def ex5(self):
        nota1 = 64
        nota2 = 45
        nota3 = 60 
        if (nota1,nota2,nota3 <= 60):
            print("Reprovado")
        else:
            print("Aprovado")
        


   



ex = exercicio()
ex.ex1()
ex.ex2()
ex.ex3()
ex.ex4()
ex.ex5()

    