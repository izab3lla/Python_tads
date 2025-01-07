from cadastros import cadastrar_disciplina, cadastrar_aluno, cadastrar_professor, cadastrar_turma, matricular_alunos, alocar_professor, filtrar_professor
from consultar import consultar_alunos, consultar_disciplina, consultar_professor

# Menu Principal
def menu():
    while True:
        print("\n[Menu]\n")
        print("Escolha uma opcao para prosseguir:")
        print("1 - Cadastrar")
        print("2 - Filtrar professores por disciplinas")
        print("3 - Matricular alunos em turmas")
        print("4 - Alocacao de professores")
        print("5 - Consultar alunos, professores, disciplinas")
        print("0 - Sair")

        opcao = input("Escolha uma opcao para prosseguir: ")

        if opcao == "1":
            menu_cadastro()
        elif opcao == "2":
            filtrar_professor()
        elif opcao == "3":
            matricular_alunos()
        elif opcao == "4":
            alocar_professor()
        elif opcao == "5":
            consultar()
        elif opcao == "0":
            print("Saindo... Ate mais!")
            break
        else:
            print("Escolha uma opcao valida!")

def menu_cadastro():
    while True:
        print("\n[Menu de Cadastro]\n")
        print("Escolha uma opcao para prosseguir:")
        print("1 - Cadastrar aluno")
        print("2 - Cadastrar professor")
        print("3 - Cadastrar disciplina")
        print("4 - Cadastrar turma")
        print("0 - Voltar")

        opcao = input("Escolha uma opcao para prosseguir: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_professor()
        elif opcao == "3":
            cadastrar_disciplina()
        elif opcao == "4":
            cadastrar_turma()
        elif opcao == "0":
            break
        else:
            print("Escolha uma opcao valida!")

def consultar():
    while True:
        print("\n[Menu de Consulta]\n")
        print("Escolha uma opcao para prosseguir:")
        print("1 - Consultar alunos matriculados em turmas")
        print("2 - Consultar professores alocados em disciplinas")
        print("3 - Consultar disciplinas ofertadas por turmas")
        print("0 - Voltar")

        opcao = input("Escolha uma opcao para prosseguir: ")

        if opcao == "1":
            consultar_alunos()
        elif opcao == "2":
            consultar_professor()
        elif opcao == "3":
            consultar_disciplina()
        elif opcao == "0":
            break
        else:
            print("Escolha uma opcao valida!")

#if _name_ == "_main_":
    menu()