alunos = []
professores = []
disciplinas = []

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

def cadastrar_disciplina():
