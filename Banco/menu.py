from banco import Conta_Corrente
from excecoes import ValorInvalidoError, SaldoInsuficienteError

def menu():
    # Criando uma conta de exemplo para os testes
    conta = Conta_Corrente("001", "Fulano", "1234", 500, 200)

    while True:
        print('\n############# BEM VINDO AO MENU DE OPERACOES ############\n')
        print('1 - Sacar')
        print('2 - Depositar')
        print('3 - Extrato')
        print('0 - Sair')

        op = input('Digite a operacao que deseja prosseguir: ')

        # Verificação para impedir crash se não for número
        try:
            op = int(op)
        except ValueError:
            print("Opção inválida")
            continue

        if op == 1:

            valor = input('Digite o valor do saque: ')
            try:
                valor = float(valor)
                conta.sacar(valor)

            except ValueError:
                print("Valor inválido! Digite um número.")
            except ValorInvalidoError as e:
                print(f"Erro: {e}")
            except SaldoInsuficienteError as e:
                print(f"Erro: {e}")

        elif op == 2:

            valor = input('Digite o valor a ser depositado: ')
            try:
                valor = float(valor)
                conta.depositar(valor)

            except ValueError:
                print("Valor inválido! Digite um número.")
            except ValorInvalidoError as e:
                print(f"Erro: {e}")

        elif op == 3:
            conta.print_extrato()

        elif op == 0:
            print('Saindo...')
            break

        else:
            print('Ops, digite uma opcao valida')


if __name__ == "__main__":
    menu()
