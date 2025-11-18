class SaldoInsuficienteError(Exception):
    """Erro quando o saque é maior que o saldo disponível."""
    pass

class LimiteExcedidoError(Exception):
    """Erro quando o saque ultrapassa o limite permitido."""
    pass

class ValorInvalidoError(Exception):
    """Erro quando o valor informado é negativo, zero ou não numérico."""
    pass

class SenhaInvalidaError(Exception):
    """Erro quando a senha informada é inválida."""
    pass

class ContaInexistenteError(Exception):
    """Erro quando a conta informada não existe."""
    pass

class OperacaoNaoPermitidaError(Exception):
    """Erro quando a operação não é permitida."""
    pass

class PrazoNaoVencidoError(Exception):
    """Erro quando o prazo do empréstimo não foi vencido."""
    pass        

class SaldoInsuficienteParaManutencaoError(Exception):
    """Erro quando o saldo é insuficiente para cobrança de taxa de manutenção."""
    pass
