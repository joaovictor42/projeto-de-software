import os
from business.control.PaymentControl import PaymentControl

payment_control = PaymentControl()

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
            payment_control.list()
        elif option == '2':
            select_request()
        else:
            print('Opção Inválida')
            input('[Enter] para continuar')


def select_request():
    os.system('clear')
    print('Selecionar Pagamento\n')

    id = int(input('ID do Pagamento: '))
    try:
        request = payment_control.select(id)
    except KeyError:
        print('\Pagamento não encontrado!')
    else:
        os.system('clear')
        request.show()

    input('[Enter] para continuar')



