from banco import sacar, depositar, extrato

def menu():

    while True:
        print('\n############# BEM VINDO AO MENU DE OPERACOES ############\n')
        print('1 - Sacar')
        print('2 - Depositar')
        print('3 - Extrato')
        print('0 - Sair')

        op = input('Digite a operacaoo que deseja prosseguir:')

        if op  == 1:
            valor = float(input('Digite o valor do saque:'))
            saldo = sacar(saldo, valor)
        
        elif op == 2:
            valor = float(input('Digite o valor a ser depositado:'))
            saldo = depositar(saldo, valor)
        
        elif op == 3:
            pass
            
        elif op == 4:
            print('Saindo...')
            break
        else:
            print('Ops, digite uma opcao valida')
                 
if __name__ == "__main__":
    menu()
