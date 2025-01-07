#pagina de consultas#
#alunos#
def consultar_alunos():
    turma_consulta  = input("Digite a turma que deseja saber os  alunos matriculados:")
    for turma in turmas:
        if turma["nome"] == turma_consulta:
         print (f"Alunos matriculados na turma: {turma_consulta}")
         for aluno in turma["alunos"]:
            print(f"{aluno}")
         return
    print ("Turma nao encontrada, tente novamente!")
