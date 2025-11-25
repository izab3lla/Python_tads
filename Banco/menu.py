from banco import Conta_Corrente
from excecoes import ValorInvalidoError, SaldoInsuficienteError, SenhaInvalidaError

def menu():
    # Criando uma conta de exemplo para os testes
    #numero da conta, titular, senha, saldo inicial, limite de saque
    conta = Conta_Corrente("001", "Fulano", "1234", 500, 200)
    # autenticação da conta
    print("===== LOGIN =====")
    senha = input("Digite sua senha: ") #pede a senha
    try:
        if not conta.autenticar(senha): #autentica a senha
            raise SenhaInvalidaError("Senha incorreta.") #levanta exceção se a senha estiver incorreta
    except SenhaInvalidaError as e: # captura a exceção
        print(e) # exibe a mensagem de erro
        return
#######################################################################

    while True:  
        print('\n#############OLÁ, nome BEM VINDO AO MENU DE OPERACOES ############\n')
        print('1 - Sacar')
        print('2 - Depositar')
        print('3 - Extrato')
        print('0 - Sair')

        op = input('Digite a operacao que deseja prosseguir: ')

        # Verificação para impedir crash se não for número
        try: 
            op = int(op) #converte a opção para inteiro
        except ValueError: # captura erro de conversão
            print("Opção inválida") 
            continue

        if op == 1:

            valor = input('Digite o valor do saque: ') #pede o valor do saque
            try:
                valor = float(valor) #converte o valor para float
                conta.sacar(valor) #tenta realizar o saque

            except ValueError:
                print("Valor inválido! Digite um número.") # captura erro de conversão
            except ValorInvalidoError as e: # captura erro de valor inválido
                print(f"Erro: {e}") # exibe a mensagem de erro
            except SaldoInsuficienteError as e: # captura erro de saldo insuficiente
                print(f"Erro: {e}") # exibe a mensagem de erro

        elif op == 2:

            valor = input('Digite o valor a ser depositado: ') #pede o valor do depósito
            try:
                valor = float(valor)
                conta.depositar(valor)

            except ValueError: 
                print("Valor inválido! Digite um número.") # captura erro de conversão
            except ValorInvalidoError as e: # captura erro de valor inválido
                print(f"Erro: {e}") # exibe a mensagem de erro

        elif op == 3:
            conta.print_extrato()

        elif op == 0:
            print('Saindo...')
            break

        else:
            print('Ops, digite uma opcao valida')
