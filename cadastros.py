import re #Import do regex

#Validacoes e cadastros#
alunos = []
professores = []
disciplinas = []
turmas = []

def cadastrar_aluno(nome, matricula, data_de_nascimento, sexo, endereco, telefone, email):
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

def cadastrar_professor(nome, matricula, data_de_nascimento, sexo, endereco, telefone, email, disciplina):
    nome = input("Nome do professor:")
    matricula = input("Matricula:")
    data_de_nascimento = int(input("Data de nascimento:(dd/mm/aaaa)"))
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

def cadastrar_disciplina(nome, codigo, carga_horaria, professor):
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

def cadastrar_turma(nome, codigo, disciplina, professor, alunos):
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