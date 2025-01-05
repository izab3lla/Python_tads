alunos = []
professores = []
disciplinas = []
turmas = []

def cadastrar_aluno(nome, matricula, data_de_nascimento, sexo, endereco, telefone, email):
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
    nome = input("Nome do aluno:")
    matricula = input("Matricula:")
    data_de_nascimento = int(input("Data de nascimento:(dd/mm/aaaa)"))
    sexo = input("Sexo: m/f")
    endereco = input("Endereco:")
    telefone = int(input("telefone:"))
    email = input("e-mail:")

def cadastrar_professor(nome, matricula, data_de_nascimento, sexo, endereco, telefone, email, disciplina):
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
    nome = input("Nome do professor:")
    matricula = input("Matricula:")
    data_de_nascimento = int(input("Data de nascimento:(dd/mm/aaaa)"))
    sexo = input("Sexo: m/f")
    endereco = input("Endereco:")
    telefone = int(input("Telefone:"))
    email = input("E-mail:")
    disciplina = input("Disciplina")

def cadastrar_disciplina(nome, codigo, carga_horaria, professor):
    disciplina = {
        "nome": nome,
        "codigo": codigo, 
        "carga_horaria": carga_horaria,
        "professor": professor
    }
    disciplinas.append(disciplina)
    nome = input("Nome da disciplina:")
    codigo = input("Digite o codigo:")
    carga_horaria = int(input("Digite a carga horaria:"))
    professor = input("Professor:")

def cadastrar_turma(nome, codigo, disciplina, professor, alunos):
    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": disciplina,
        "professor": professor,
        "alunos": alunos
    }
    turmas.append(turma)
    nome = input("Nome da disciplina:")
    codigo = input("Digite o codigo:")
    disciplina = input("Digite a disciplina:")
    professor = input("Professor:")
    alunos = input("Alunos:")