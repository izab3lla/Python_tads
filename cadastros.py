import re
import uuid

# Listas globais para armazenar os dados
# Dados predefinidos para testes | Dado Mockado  
alunos = [
    {"nome": "Alice", "matricula": str(uuid.uuid4()), "data_de_nascimento": "01/01/2005", "sexo": "f", "endereco": "Rua A, 123", "telefone": "(11) 98765-4321", "email": "alice@gmail.com"},
    {"nome": "Bob", "matricula": str(uuid.uuid4()), "data_de_nascimento": "15/05/2004", "sexo": "m", "endereco": "Rua B, 456", "telefone": "(22) 98765-1234", "email": "bob@gmail.com"}
]

professores = [
    {"nome": "Carlos", "matricula": str(uuid.uuid4()), "data_de_nascimento": "20/03/1980", "sexo": "m", "endereco": "Rua C, 789", "telefone": "(33) 91234-5678", "email": "carlos@gmail.com", "disciplina": "Matemática"},
    {"nome": "Diana", "matricula": str(uuid.uuid4()), "data_de_nascimento": "10/07/1985", "sexo": "f", "endereco": "Rua D, 101", "telefone": "(44) 98765-4321", "email": "diana@gmail.com", "disciplina": "Português"}
]

disciplinas = [
    {"nome": "Matemática", "codigo": str(uuid.uuid4()), "carga_horaria": 40, "professor": "Carlos"},
    {"nome": "Português", "codigo": str(uuid.uuid4()), "carga_horaria": 30, "professor": "Diana"}
]

turmas = [
    {"nome": "Turma A", "codigo": str(uuid.uuid4()), "disciplina": "Matemática", "professor": "Carlos", "alunos": ["Alice", "Bob"]},
    {"nome": "Turma B", "codigo": str(uuid.uuid4()), "disciplina": "Português", "professor": "Diana", "alunos": []}
]

# Funções de Cadastro
def cadastrar_aluno():
    print("\n+ Cadastro de aluno +\n")
    nome = input("Nome do aluno: ")
    matricula = str(uuid.uuid4())
    data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    sexo = validar_sexo()
    endereco = input("Endereco: ")
    telefone = input("Telefone: ") # validar_telefone()
    email = input("e-mail: ")

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
    print(f"Aluno {nome} cadastrado com sucesso! Matricula: {matricula}")

def cadastrar_professor():
    print("\n+ Cadastro de Professor +\n")
    nome = input("Nome do professor: ")
    matricula = str(uuid.uuid4())
    data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    sexo = validar_sexo()
    endereco = input("Endereco: ")
    telefone = input("Telefone: ") # validar_telefone()
    email = input("E-mail: ")
    disciplina = input("Disciplina: ")

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
    print(f"Professor {nome} cadastrado com sucesso! Matricula: {matricula}")

def cadastrar_disciplina():
    print("\n+ Cadastro de disciplina +\n")
    nome = input("Nome da disciplina: ")
    codigo = str(uuid.uuid4())
    carga_horaria = int(input("Digite a carga horaria: "))

    disciplina = {
        "nome": nome,
        "codigo": codigo, 
        "carga_horaria": carga_horaria,
        "professor": None  # Inicialmente sem professor
    }
    disciplinas.append(disciplina)
    print(f"Disciplina {nome} cadastrada com sucesso! Codigo: {codigo}")

def cadastrar_turma():
    print("\n+ Cadastro de turma +\n")
    nome = input("Nome da turma: ")
    codigo = str(uuid.uuid4())

    turma = {
        "nome": nome,
        "codigo": codigo,
        "disciplina": None,
        "professor": None,
        "alunos": []
    }
    turmas.append(turma)
    print(f"Turma {nome} cadastrada com sucesso! Codigo: {codigo}")
# Funções de Alocação
def matricular_alunos():
    print("\n+ Matricular alunos em turmas +\n")
    nome_do_aluno = input("Digite o nome do aluno: ")
    nome_da_turma = input("Digite a turma que deseja matricular o aluno: ")

    aluno = next((aluno for aluno in alunos if aluno["nome"] == nome_do_aluno), None)
    turma = next((turma for turma in turmas if turma["nome"] == nome_da_turma), None)

    if not aluno:
        print("Aluno não encontrado!")
        return

    if not turma:
        print("Turma não encontrada!")
        return

    turma["alunos"].append(aluno["nome"])
    print(f"Aluno {nome_do_aluno} matriculado na turma {nome_da_turma}!")

def alocar_professor():
    print("\n+ Alocacao de professor +\n")
    nome_professor = input("Digite o nome do professor a ser alocado: ")
    nome_disciplina = input("Digite o nome da disciplina: ")

    professor = next((prof for prof in professores if prof["nome"] == nome_professor), None)
    disciplina = next((disc for disc in disciplinas if disc["nome"] == nome_disciplina), None)

    if not professor:
        print("Professor não encontrado!")
        return

    if not disciplina:
        print("Disciplina não encontrada!")
        return

    disciplina["professor"] = professor["nome"]
    print(f"Professor {nome_professor} alocado na disciplina {nome_disciplina}!")

def filtrar_professor():
    print("\n+ Filtrar Professores por Disciplinas +\n")
    nome_disciplina = input("Digite o nome da disciplina: ")
    
    # Busca pela disciplina
    disciplina = next((disc for disc in disciplinas if disc["nome"] == nome_disciplina), None)
    
    if not disciplina:
        print("Disciplina não encontrada!")
        return

    professor = disciplina["professor"]
    if professor:
        print(f"Professor alocado na disciplina {nome_disciplina}: {professor}")
    else:
        print(f"Nenhum professor alocado para a disciplina {nome_disciplina}.")
   

# Funções de Validação
def validar_sexo():
    while True:
        sexo = input("Digite o sexo (m/f): ").lower()
        if sexo in ("m", "f"):
            return sexo
        print("Sexo inválido, tente novamente!")