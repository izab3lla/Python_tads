def menu():
    while True:
        print("Escolha uma opcao para prosseguir:")
        print("1 - Cadastrar")
        print("2 - Filtrar professores por disciplinas")
        print("3 - Matricular alunos em turmas")
        print("4 - Alocacao de professores")
        print("5 - Consultar alunos, professores, disciplinas")
        print("0 - Sair")

        opcao = input("Escolha uma opcao para prosseguir:")
        if opcao == 1:
            menu_cadastro()
        elif opcao == 2:
            filtrar_professor()
        elif opcao == 3:
            matricular_alunos()
        elif opcao == 4:
            alocar_professor()
        elif opcao == 5:
            consultar()
        elif opcao == 0:
            break
        else:
            print("Escolha uma opcao valida")

def menu_cadastro():
    while True:
        print("Menu de cadastro \n")
        print ("Escolha uma opcao para prosseguir:")
        print ("1 - Cadastrar aluno")
        print ("2 - Cadastrar Professor")
        print ("3 - Cadastrar disciplina")
        print ("4 - Cadastrar turma")
        print ("0 - Sair")

def consultar():
        print("Menu de consulta \n")
        print ("Escolha uma opcao para prosseguir:")
        print ("1 - consultar Alunos metriculados em turmas")
        print ("2 - Consultar professores alocados em disciplinas")
        print ("3 - Consultar Disciplinas alocadas por turmas")
        print ("0 - Sair")
    