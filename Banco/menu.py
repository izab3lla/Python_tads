from banco import Conta_Corrente

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
        #essa verificação é para evitar que o programa quebre caso o usuário digite algo que não seja número
        try:
            op = int(op)
        except: 
            print("Opção inválida")
            continue

        if op == 1:
            valor = float(input('Digite o valor do saque: '))
            conta.sacar(valor)

        elif op == 2:
            valor = float(input('Digite o valor a ser depositado: '))
            conta.depositar(valor)

        elif op == 3:
            conta.print_extrato()

        elif op == 0:
            print('Saindo...')
            break

        else:
            print('Ops, digite uma opcao valida')


if __name__ == "__main__":
    menu()
