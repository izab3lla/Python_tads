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

#professor#
def consultar_professor():
   professor_consulta = input("Digite  a disciplina para saber os professores alocados nela:")
   for disciplina in disciplinas:
      if  disciplina["nome"] == professor_consulta:
         print (f"Professores alocados na disciplina:{professor_consulta}")
         return
      else:
         print("Nenhum professor alocado para esta disciplina, tente novamente!")

#disciplina#
def consultar_disciplina():
    turmas_por_disciplinas = input("Digite a turma que deseja saber as disciplinas ofertadas:")
    for turma in turmas:
       if turma["nome"] == turmas_por_disciplinas:
          print(f"As disciplinas ofertadas na turma {turmas_por_disciplinas}:")
          for disciplina in turma["disciplina"]:
             print(f"- {disciplina}")
          return
    else:
       print("Turma nao encontrada, tente novamente!")