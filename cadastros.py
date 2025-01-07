import re #Import do regex

#Validacoes e cadastros#
alunos = []
professores = []
disciplinas = []
turmas = []

def cadastrar_aluno():
    nome = input("Nome do aluno:")
    matricula = input("Matricula:")
    data_de_nascimento = int(input("Data de nascimento:(dd/mm/aaaa)"))
    sexo = validar_sexo()
    endereco = input("Endereco:")
    telefone = validar_telefone()
    email = input("e-mail:")

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "data_de_nascimento": data_de_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email
    }
    alunos.append(aluno)

def cadastrar_professor():
    nome = input("Nome do professor:")
    matricula = input("Matricula:")
    data_de_nascimento = int(input("Data de nascimento(dd/mm/aaaa):"))
    sexo = validar_sexo()
    endereco = input("Endereco:")
    telefone = validar_telefone()
    email = input("E-mail:")
    disciplina = input("Disciplina:")

    professor = {
        "nome": nome,
        "matricula": matricula,
        "data_de_nascimento": data_de_nascimento,
        "sexo": sexo,
        "endereco": endereco,
        "telefone": telefone,
        "email": email,
        "disciplina": disciplina
    }
    professores.append(professor)

def cadastrar_disciplina():
    nome = input("Nome da disciplina:")
    codigo = input("Digite o codigo:")
    carga_horaria = int(input("Digite a carga horaria:"))
    professor = input("Professor:")

    disciplina = {
        "nome": nome,
        "codigo": codigo, 
        "carga_horaria": carga_horaria,
        "professor": professor
    }
    disciplinas.append(disciplina)

def cadastrar_turma():
    nome = input("Nome da disciplina:")
    codigo = input("Digite o codigo:")
    disciplina = input("Digite a disciplina:")
    professor = input("Professor:")
    alunos = input("Alunos:")

    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": disciplina,
        "professor": professor,
        "alunos": alunos
    }
    turmas.append(turma)

#arrumar isso aquiiiii
def matricular_alunos():
    nome_do_aluno = input("Digite o nome do aluno:")
    nome_da_turma = input("Digite a turma que deseja matricular o aluno:")

    turma_existe = None
    for turma in turmas:
        if turma["nome"] == nome_da_turma:
            turma_existe = turma
            break
    turma_existe["alunos"].append(nome_do_aluno)

    #alocacao de professor
def alocar_professor():
    nome_professor = input("Digite  o nome do professor a ser alocado: ")
    nome_disciplina = input("Digite o nome da disciplina:")
    for disciplina in disciplinas:
        if disciplina["nome"] == nome_disciplina:
            disciplina["professor"] = nome_professor
    print(f"Professor foi alocado na disciiplina {nome_disciplina} com sucesso!")

def validar_sexo():
    sexo = input("Digite o sexo (m/f):").lower() #se colocar maiusculo vai alterar aceitar tambem#
    if sexo == "m" or sexo == "f":
        return sexo
    else:
        print("Sexo invalido, tente novamente")

def validar_telefone():
    padrao = r"^\(\d{2}\) \d{5}-\d{4}$"
    while True:
        telefone = input("Insira o numero telefone ((dd)xxxxx-xxxxx):")
        if not re.match(padrao, telefone):
            print("Numero de telefone invalido, tente novamente!")
            break

def filtrar_professor():
    nome_disciplina = input("Digite o nome da disciplina:")

    if nome_disciplina in disciplinas:
        print(f"Professores alocados na disciplina {disciplinas[nome_disciplina]}")
    else: 
        print ("Nenhum professor encontrado, tente novamente!")