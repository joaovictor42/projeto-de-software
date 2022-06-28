from business.control.SystemControl import SystemControl
import os

system = SystemControl()


def pay_manager_view():
    while True:
        os.system('clear')
        print('Gerencimento de Pagamentos\n')
        print('1 - Listar Pagamentos')
        print('2 - Selecionar Pagamento')
        print('0 - Voltar\n')

        option = input('Opção: ')
        if option == '0':
            return
        elif option == '1':
            system.payment_control.list()
        elif option == '2':
            select_request()
        else:
            print('Opção Inválida')
            input('[Enter] para continuar')


def select_request():
    os.system('clear')
    print('Selecionar Pagamento\n')

    try:
        id = int(input('ID do Pagamento: '))
        request = system.payment_control.select(id)
    except:
        print('\Pagamento não encontrado!')
    else:
        os.system('clear')
        request.show()

    input('[Enter] para continuar')



