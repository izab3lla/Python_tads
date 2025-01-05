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
            return
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

        opcao_cadastro = input("Escolha uma opcao para prosseguir:")
        if opcao_cadastro == 1:
            cadastrar_aluno()
        elif opcao_cadastro == 2:
            cadastrar_professor()
        elif opcao_cadastro == 3:
            cadastrar_disciplina()
        elif opcao_cadastro == 4:
            cadastrar_turma()
        elif opcao_cadastro == 0:
            return
        else:
            print("Escolha uma opcao valida")


def consultar():
        print("Menu de consulta \n")
        print ("Escolha uma opcao para prosseguir:")
        print ("1 - consultar Alunos metriculados em turmas")
        print ("2 - Consultar professores alocados em disciplinas")
        print ("3 - Consultar Disciplinas alocadas por turmas")
        print ("0 - Sair")

        pcao_consulta = input("Escolha uma opcao para prosseguir: ")

        if opcao_consulta == 1: 
            consulta_aluno()
        elif opcao_consulta == 2:  
            consulta_professor()
        elif opcao_consulta == 3:  
            consulta_disciplina()
        elif opcao_consulta == 0: 
            return 
        else:
            print("Escolha uma opcao valida")

menu()