import hashlib
from datetime import datetime
from excecoes import SaldoInsuficienteException, LimiteExcedidoException, ValorInvalidoException, SaldoInsuficienteParaManutencaoException

# =========================
# Classe Endereco 
# =========================
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


# =========================
# Classe Pessoa 
# =========================
class Pessoa:
    def __init__(self, id: str, cpf: str, nome: str):
        self._id = id
        self._cpf = cpf
        self._nome = nome

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        self._nome = value


# =========================
# Classe Banco
# =========================
class Banco:
    def __init__(self, cnpj: str, nome: str, agencia: str):
        self.__cnpj = cnpj
        self.__nome = nome
        # inicializo como lista vazia (agências serão adicionadas com método)
        self.__agencia = []
        self.contas = []
        self.funcionarios = []

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, value):
        self.__cnpj = value

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def agencia(self):
        return self.__agencia
    @agencia.setter
    def agencia(self, value):
        self.__agencia = value

    def adicionar_agencia(self, agencia):
        # append na lista privada de agências
        self.__agencia.append(agencia)

    # método auxiliar que cria e adiciona agência 
    def criar_e_adicionar_agencia(self, numero: str, nome: str, endereco: str, fone: str):
        a = Agencia(numero, nome, endereco, fone)
        self.adicionar_agencia(a)
        return a


# =========================
# Classe Agencia
# =========================
class Agencia:
    def __init__(self, numero: str, nome: str, endereco: str, fone: str):
        self.__numero = numero
        self._nome = nome
        self._endereco = endereco
        self._fone = fone
        # inicialização correta da lista de contas (evita forward-ref issues)
        self._conta = []

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

    # adiciona conta à lista interna de contas
    def adicionar_conta(self, conta: 'Conta'):  # referência futura aceita como string
        self._conta.append(conta)

    # buscar conta pela número 
    def buscar_conta(self, numero: str):
        for c in self._conta:
            if c.numero == numero:
                return c
        return None


# =========================
# Classe Cliente 
# =========================
class Cliente(Pessoa):
    def __init__(self, id: str, cpf: str, nome: str, email: str, data_nascimento: str):
        # chama o construtor da superclasse para manter herança coerente
        super().__init__(id, cpf, nome)
        # atributos específicos de Cliente
        self.__email = email
        self.__data_nascimento = data_nascimento

    # note: reuso os atributos da superclasse (self._nome, self._id, self._cpf)
    @property  # transforma método em propriedade
    def nome(self):
        # retorna nome vindo de Pessoa
        return self._nome

    @nome.setter
    def nome(self, nome):
        # corrigi recursão e seto o atributo herdado
        self._nome = nome

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f"Cliente: {self._nome} | CPF: {self._cpf} | Email: {self.__email}"


# =========================
# Classe Funcionario 
# =========================
class Funcionario(Pessoa):
    def __init__(self, id: str, cpf: str, nome: str, matricula: str, dt_nasc: str):
        # chama o construtor da superclasse
        super().__init__(id, cpf, nome)
        self.__matricula = matricula
        self.__dt_nasc = dt_nasc

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def dt_nasc(self):
        return self.__dt_nasc
    @dt_nasc.setter
    def dt_nasc(self, dt_nasc):
        self.__dt_nasc = dt_nasc


# =========================
# Classe Transacao
# =========================
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


# =========================
# Classe Conta 
# =========================
class Conta:
    def __init__(self, numero: str, titular: str, saldo: float, senha: str):
        self._numero = numero
        self._titular = titular  
        if saldo < 0:
            raise ValorInvalidoException("Saldo inicial inválido.")
        self._saldo = saldo
        # armazenar senha como hash para não manter senha em texto claro
        self._senha_hash = self._hash_pwd(senha)
        # inicialização correta da lista de transações
        self._transacoes = []

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
        # não retornar a senha em texto claro
        return "<oculta>"
    @senha.setter
    def senha(self, value):
        self._senha_hash = self._hash_pwd(value)

    def _hash_pwd(self, pwd: str) -> str:
        """Retorna o hash SHA-256 da senha passada."""
        if pwd is None:
            return ""
        return hashlib.sha256(pwd.encode("utf-8")).hexdigest()

    def add_transacao(self, transacao: Transacao):
        self._transacoes.append(transacao)

    def autenticar(self, pwd: str) -> bool:
        return self._senha_hash == self._hash_pwd(pwd)

    def sacar(self, valor: float):
        # adicionada verificação básica de saldo e registro de transação
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValorInvalidoException("Valor do saque deve ser maior que zero.") # lança exceção

        if valor > self._saldo:
            raise SaldoInsuficienteException("Saldo insuficiente para saque.") # lança exceção

        self._saldo -= valor
        self._transacoes.append(Transacao("Saque", valor, self))
        return True

    def depositar(self, valor: float):
        # adicionada verificação básica e registro de transação
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValorInvalidoException("Valor de depósito inválido.") # lança exceção
        self._saldo += valor
        self._transacoes.append(Transacao("Depósito", valor, self))
        return True

    def extrato(self):  # retorna uma lista de strings com as transações
        lista = []
        for t in self._transacoes:
            # usei propriedades de Transacao (data, tipo, valor)
            lista.append(f"{t.data.strftime('%Y-%m-%d %H:%M:%S')} - {t.tipo} - R${t.valor:.2f}")
        return lista

    def __repr__(self):
        return f"<Conta numero={self._numero} titular={self._titular} saldo={self._saldo:.2f}>"

    def print_extrato(self):
        print("==== EXTRATO ====")
        print(f"Conta: {self._numero}")
        print(f"Titular: {self._titular}")
        print("------------------")

        if len(self._transacoes) == 0:
            print("Nenhuma transação realizada.")
        else:
            for t in self._transacoes:
                print(f"{t.data.strftime('%Y-%m-%d %H:%M:%S')} | {t.tipo} | R${t.valor:.2f}")

        print("------------------")
        print(f"Saldo atual: R${self._saldo:.2f}")

    def transferir(self, valor: float, destino: 'Conta') -> bool:
        """Transfere valor para outra conta, verificando saldo e limite (se houver)."""
        if valor <= 0:
            raise ValorInvalidoException("Valor de transferência inválido.")

        total_disponivel = self._saldo + getattr(self, '_limite', 0)
        if valor > total_disponivel:
            raise LimiteExcedidoException("Limite insuficiente para transferência.")

        self._saldo -= valor
        destino._saldo += valor
        self._transacoes.append(Transacao("Transferência enviada", valor, self))
        destino._transacoes.append(Transacao("Transferência recebida", valor, destino))
        return True


# =========================
# Conta Corrente
# =========================
class Conta_Corrente(Conta):
    def __init__(self, numero: str, titular: str, pwd: str, saldo: float, limite: float):
        # Conta espera: numero, titular, saldo, senha
        # Aqui a ordem é: numero, titular, senha, saldo, limite
        super().__init__(numero, titular, saldo, pwd)
        if limite < 0:
            raise ValorInvalidoException("Limite inválido.")
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

    def cobrar_manutencao(self): # cobra a taxa de manutenção se houver saldo suficiente
        if self._saldo >= self._tx_manutencao:
            self._saldo -= self._tx_manutencao
            self._transacoes.append(Transacao("Taxa Manutenção", self._tx_manutencao, self))
            return True
        raise SaldoInsuficienteParaManutencaoException("Saldo insuficiente para cobrança de taxa de manutenção.")

# =========================
# Conta Poupança
# =========================
class Conta_poupanca(Conta):
    def __init__(self, numero: str, titular: str, pwd: str, saldo: float, tx_juros: float):
        # Conta espera: numero, titular, saldo, senha
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
        return super().sacar(valor)

    def render_juros(self):  # verifica se é dia de aniversario e aplica os juros
        hoje = datetime.now().day  # pega o dia atual
        if hoje == self._aniversario:  # compara com o dia de aniversario
            rendimento = self._saldo * self._tx_juros  # calcula o rendimento
            self._saldo += rendimento  # adiciona ao saldo
            self._transacoes.append(Transacao("Rendimento Poupança", rendimento, self))
            return rendimento  # retorna o valor do rendimento
        return 0  # se não for dia de aniversario retorna 0

    def aplicar(self, valor: float):  # adiciona valor ao saldo
        if valor > 0:  # verifica se o valor é positivo
            self._saldo += valor  # se sim adiciona ao saldo
            self._transacoes.append(Transacao("Aplicação", valor, self))
            return True
        raise ValorInvalidoException("Valor de aplicação inválido.")  # lança exceção

# =========================
# Classe Emprestimo
# =========================
class Emprestimo:
    def __init__(self, valor: float, taxa_juros: float, prazo: int, conta: Conta):
        self._valor = valor
        self._taxa_juros = taxa_juros
        self._prazo = prazo
        self._conta = conta
        self._data_transacao = datetime.now()
        # calcula parcela ao criar
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
    def data_transacao(self):
        return self._data_transacao
    @data_transacao.setter
    def data_transacao(self, value):
        self._data_transacao = value

    @property
    def valor_parcela(self):
        return self._valor_parcela
    @valor_parcela.setter
    def valor_parcela(self, value):
        self._valor_parcela = value

    def calcular_parcela(self):  # calcula o valor da parcela mensal do empréstimo
        # Fórmula da parcela mensal do empréstimo:
        i = self._taxa_juros  # taxa de juros mensal em decimal
        n = self._prazo  # número de parcelas

        if n == 0:
            raise ValorInvalidoException("Prazo do empréstimo deve ser maior que zero.")

        if i == 0:
            # se a taxa de juros for 0, parcela é valor dividido pelo número de parcelas
            return self._valor / n

        parcela = self._valor * (i * (1 + i) ** n) / ((1 + i) ** n - 1)  # fórmula da parcela mensal
        return parcela

