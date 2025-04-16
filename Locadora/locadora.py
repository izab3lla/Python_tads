class Funcio:
    def __init__(self, nome: str, cpf: str, cargo: str, matricula: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__cargo = cargo
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.cpf = cpf

    @property
    def cargo(self):
        return self.__cargo
    @cargo.setter
    def cargo(self, cargo):
        self.cargo = cargo

    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.matricula = matricula

class Cliente:
    def __init__(self, nome: str, cpf: str, email: str, dt_nasc: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__dt_nasc = dt_nasc

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome

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

    @property
    def dt_nasc(self):
        return self.__dt_nasc
    @dt_nasc.setter
    def dt_nasc(self, dt_nasc):
        self.dt_nasc = dt_nasc

class Veiculo:
    def __init__(self, placa: str, modelo: str, ano:int, preco_base: float):
        self.__placa = placa
        self.__modelo = modelo
        self.__ano = ano
        self.__preco_base = preco_base

    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, placa):
        self.placa = placa

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.modelo = modelo

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, ano):
        self.ano = ano

    @property
    def preco_base(self):
        return self.__preco_base
    @preco_base.setter
    def preco_base(self, preco_base):
        self.preco_base = preco_base

class Filial:
    def __init__(self, numero: int, endereco: str, cliente: Cliente, funcio: Funcio, veiculo: Veiculo):
        self.__numero = numero
        self.__endereco = endereco
        self.__cliente = cliente
        self.__funcio = funcio
        self.__veiculo = veiculo

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.numero = numero

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.endereco = endereco

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.cliente = cliente

    @property
    def funcio(self):
        return self.__funcio
    @funcio.setter
    def funcio(self, funcio):
        self.funcio = funcio
    
    @property
    def veiculo(self):
        return self.__veiculo
    @veiculo.setter
    def veiculo(self, veiculo):
        self.veiculo = veiculo

class Locacao:
    def __init__(self, cliente: Cliente, tempo_locado: str, data_locacao:str, veiculo:Veiculo, preco_km: float):
        self.__cliente = cliente
        self.__tempo_locado = tempo_locado
        self.__data_locacao = data_locacao
        self.__veiculo = veiculo
        self.__preco_km = preco_km

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.cliente = cliente

    @property
    def tempo_locado(self):
        return self.__tempo_locado
    @tempo_locado.setter
    def tempo_locado(self, tempo_locado):
        self.tempo_locado = tempo_locado

    @property
    def data_locacao(self):
        return self.__data_locacao
    @data_locacao.setter
    def data_locacao(self, data_locacao):
        self.data_locacao = data_locacao

    @property
    def veiculo(self):
        return self.__veiculo
    @veiculo.setter
    def veiculo(self, veiculo):
        self.veiculo = veiculo

    @property
    def preco_km(self):
        return self.__preco_km
    @preco_km.setter
    def preco_km(self, preco_km):
        self.preco_km = preco_km

class Lista_espera:
    def __init__(self, cliente: Cliente, dt_prev: str, veiculo: Veiculo):
        self.__cliente = cliente
        self.__dt_prev = dt_prev
        self.__veiculo = veiculo

    @property
    def cliente(self):
        return self.__cliente
    @cliente.setter
    def cliente(self, cliente):
        self.cliente = cliente

    @property
    def dt_prev(self):
        return self.__dt_prev
    @dt_prev.setter
    def dt_prev(self, dt_prev):
        self.dt_prev = dt_prev

    @property
    def veiculo(self):
        return self.__veiculo
    @veiculo.setter
    def veiculo(self, veiculo):
        self.veiculo = veiculo
    
class Locadora:
    def __init__(self, cnpj: str, filial: Filial, nome: str):
        self.__cnpj = cnpj
        self.__filial = filial
        self.__nome = nome

    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.cnpj = cnpj

    @property
    def filial(self):
        return self.__filial
    @filial.setter
    def filial(self, filial):
        self.filial = filial

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.nome = nome