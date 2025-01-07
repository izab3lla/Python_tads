from cadastros import turmas, disciplinas
#alunos#
# Funcoes de Consulta
def consultar_alunos():
    turma_consulta = input("Digite a turma que deseja saber os alunos matriculados: ")
    turma = next((turma for turma in turmas if turma["nome"] == turma_consulta), None)

    if not turma:
        print("Turma nao encontrada!")
        return

    print(f"Alunos matriculados na turma {turma_consulta}:")
    for aluno in turma["alunos"]:
        print(f"- {aluno}")

def consultar_professor():
    disciplina_consulta = input("Digite a disciplina para saber os professores alocados nela: ")
    disciplina = next((disc for disc in disciplinas if disc["nome"] == disciplina_consulta), None)

    if not disciplina:
        print("Disciplina nao encontrada!")
        return

    professor = disciplina["professor"] or "Nenhum professor alocado"
    print(f"Professor alocado na disciplina {disciplina_consulta}: {professor}")

def consultar_disciplina():
    turma_consulta = input("Digite a turma que deseja saber as disciplinas ofertadas: ")
    turma = next((turma for turma in turmas if turma["nome"] == turma_consulta), None)

    if not turma:
        print("Turma nao encontrada!")
        return

    disciplina = turma["disciplina"] or "Nenhuma disciplina alocada"
    print(f"Disciplinas ofertadas na turma {turma_consulta}: {disciplina}")