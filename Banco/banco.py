import uuid
from typing import List
from datetime import datetime

class Endereco:
    def __init__(self, rua: str, bairro: str, cidade: str, estado: str, cep: str):
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__cep = cep

    @property
    def _rua(self):
        return self.__rua
    @_rua.setter
    def _rua(self, value):
        self.__rua = value

    @property
    def _bairro(self):
        return self.__bairro
    @_bairro.setter
    def _bairro(self, value):
        self.__bairro = value

    @property
    def _cidade(self):
        return self.__cidade
    @_cidade.setter
    def _cidade(self, value):
        self.__cidade = value

    @property
    def _estado(self):
        return self.__estado
    @_estado.setter
    def _estado(self, value):
        self.__estado = value

    @property
    def _cep(self):
        return self.__cep
    @_cep.setter
    def _cep(self, value):
        self.__cep = value

class Pessoa:
    pass 

class Banco:
    def __init__(self, cnpj: str, nome: str, agencia: str):
        self.__cnpj = cnpj
        self.__nome = nome
        self.__agencia = []

        self.contas = []
        self.funcionarios = []

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.cnpj = cnpj

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, agencia):
        self.agencia = list[agencia] = []

    def adicionar_agencia (self, agencia):
        self.agencia.append(agencia)
    
class Agencia:
    def __init__(self, numero: str, nome:str, endereco:str, fone:str):
        self.__numero = numero
        self._nome = nome
        self._endereco = endereco
        self._fone = fone
        self._conta: list[Conta] = []

    @property
    def _numero(self):
        return self.__numero
    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, value):
        self._endereco = value

    @property
    def fone(self):
        return self._fone
    @fone.setter
    def fone(self, value):
        self._fone = value

    #@property
    #def conta: list[Conta](self):
    #return self._conta: list[Conta]
    #@conta: list[Conta].setter
    #def conta: list[Conta](self, value):
       # self._conta: list[Conta] = value

    def adicionar_conta (self, conta: 'Conta'): #referencia futura
        self.conta.append(conta)

class Cliente(Pessoa):
    def __init__(self, id: str, cpf: str, nome: str, email: str, data_nascimento: str):
        self.__id = id
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__data_nascimento = data_nascimento

    @property #tem a propriedade de tornar um metodo propriedade
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.id = id

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.email = email

    def __str__(self):
        pass

class Funcionario(Pessoa):
    def __init__(self, id: str, cpf: str, nome: str, matricula: str, dt_nasc: str):
        self.__id = id
        self.__cpf = cpf
        self.__nome = nome
        self.__matricula = matricula
        self.__dt_nasc = dt_nasc

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.id = id

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.nome = matricula
    
    @property
    def dt_nasc(self):
        return self.__dt_nasc
    @dt_nasc.setter
    def dt_nac(self, dt_nasc):
        self.dt_nasc = dt_nasc
    
class Transacao:
    def __init__(self, tipo: str, valor: float, conta: 'Conta'):
        self._tipo = tipo
        self._valor = valor
        self._data = datetime.now()
        self._conta = conta

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self, value):
        self._conta = value

class Conta:
    def __init__(self, numero: str, titular: str, saldo: float, senha: str):
        self._numero = numero
        self._titular = titular #tem que arrumar esse trem
        self._saldo = saldo
        self._senha = senha
        self._transacoes = list[Transacao] = []

    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, value):
        self._numero = value

    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self, value):
        self._titular = value

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, value):
        self._saldo = value

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, value):
        self._senha = value

    def add_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)

    def autenticar(self, pwd: str) -> bool:
        return self._senha == pwd
    
    def sacar(self, valor: float):
        self.saldo -= valor
    
    def depositar(self, valor: float):
        self.saldo += valor
    
    def extrato(self):
        lista = []
        for t in self._transacoes:
            lista.append(f"{t.data} - {t.tipo} - R${t.valor:.2f}")
        return lista
        
    def print_extrato(self):
        print("==== EXTRATO ====")
        print(f"Conta: {self._numero}")
        print(f"Titular: {self._titular}")
        print("------------------")

        if len(self._transacoes) == 0:
            print("Nenhuma movimentação.")
        else:
            for t in self._transacoes:
                print(f"{t.data} | {t.tipo} | R${t.valor:.2f}")

        print("------------------")
        print(f"Saldo atual: R${self._saldo:.2f}")

class Conta_Corrente(Conta):
    def __init__(self, numero: str, titular: str, pwd: float, saldo:float, limite:float):
        super().__init__(numero, titular, pwd, saldo)
        self._limite = limite
        self._tx_manutencao = 10.0

    @property
    def limite(self):
        return self._limite
    @limite.setter
    def limite(self, value):
        self._limite = value

    @property
    def tx_manutencao(self):
        return self._tx_manutencao
    @tx_manutencao.setter
    def tx_manutencao(self, value):
        self._tx_manutencao = value

class Conta_poupanca(Conta):
    def __init__(self, numero: str, titular: str, pwd: float, saldo:float, tx_juros: float):
       super().__init__(numero, titular, saldo, pwd)
       self._tx_juros = tx_juros
       self._aniversario = datetime.now().day
    

    @property
    def tx_juros(self):
        return self._tx_juros
    @tx_juros.setter
    def tx_juros(self, value):
        self._tx_juros = value

    @property
    def aniversario(self):
        return self._aniversario
    @aniversario.setter
    def aniversario(self, value):
        self._aniversario = value

    def sacar(self, valor: float):
        self.saldo -= valor

    def render_juros(self):
        hoje = datetime.now().day 
        if hoje == self._aniversario:
            rendimento = self._saldo * self._tx_juros
            self._saldo += rendimento
            return rendimento
        return 0
    
    def aplicar (self, valor: float):
        if valor > 0:
            self._saldo += valor
            self._transacoes.append(Transacao("Aplicação", valor, self))

class Emprestimo:
    def __init__(self, valor: float, taxa_juros: float, prazo: int, conta: Conta):
        self._valor = valor
        self._taxa_juros = taxa_juros
        self._prazo = prazo
        self._conta = conta
        self._data_transa = datetime.now
        self._valor_parcela = self.calcular_parcela()

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, value):
        self._valor = value

    @property
    def taxa_juros(self):
        return self._taxa_juros
    @taxa_juros.setter
    def taxa_juros(self, value):
        self._taxa_juros = value

    @property
    def prazo(self):
        return self._prazo
    @prazo.setter
    def prazo(self, value):
        self._prazo = value

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self, value):
        self._conta = value

    @property
    def data_transa(self):
        return self._data_transa
    @data_transa.setter
    def data_transa(self, value):
        self._data_transa = value

    @property
    def valor_parcela(self):
        return self._valor_parcela
    @valor_parcela.setter
    def valor_parcela(self, value):
        self._valor_parcela = value
    
    
    def calcular_parcela():
        pass

cliente_x = Cliente("a43v", "435.542.543-65", "xyz", "a@gmail.com", "10/03/2004")
print(cliente_x.nome)
print(cliente_x.id)
print(cliente_x.cpf)
print(cliente_x.email)
print("\n")

cliente_y = Cliente("43c24", "764.765.423-65", "abc", "y@gmail.com", "43/76/1009")
print(cliente_y.nome)
print(cliente_y.id)

Funcionario_a = Funcionario("a324b", "098.987.875-45", "cleber", "3434", "28/05/2054")
print(Funcionario_a.nome)
print(Funcionario_a.id)

Conta_coco_1 = Conta_Corrente ("a", "brasil", "cliente_x")

conta_poup_1 = Conta_poupanca("3245", "a", "itau", "cliente_y")

banc_1 = Banco("cliente_x", "brasil", "cleber", "a")