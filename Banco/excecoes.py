class SaldoInsuficienteException(Exception):
    """Erro quando o saque é maior que o saldo disponível."""
    pass

class LimiteExcedidoException(Exception):
    """Erro quando o saque ultrapassa o limite permitido."""
    pass

class ValorInvalidoException(Exception):
    """Erro quando o valor informado é negativo, zero ou não numérico."""
    pass

class SenhaInvalidaException(Exception):
    """Erro quando a senha informada é inválida."""
    pass

class ContaInexistenteException(Exception):
    """Erro quando a conta informada não existe."""
    pass

class OperacaoNaoPermitidaException(Exception):
    """Erro quando a operação não é permitida."""
    pass

class SaldoInsuficienteParaManutencaoException(Exception):
    """Erro quando o saldo é insuficiente para cobrança de taxa de manutenção."""
    pass
