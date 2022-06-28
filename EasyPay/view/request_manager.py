import os
from business.control.RequestControl import RequestControl

request_control = RequestControl()

def request_manager_view():
    while True:
        os.system('clear')
        print('Gerencimento de Solicitações\n')
        print('1 - Listar Solicitações')
        print('2 - Selecionar Solicitação')
        print('3 - Deletar Solicitação')
        print('0 - Voltar\n')

        option = input('Opção: ')
        if option == '0':
            return
        elif option == '1':
            request_control.list()
        elif option == '2':
            select_request()
        elif option == '3':
            del_request()
        else:
            print('Opção Inválida')
            input('[Enter] para continuar')


def select_request():
    os.system('clear')
    print('Selecionar Solicitação\n')

    id = int(input('ID da Solicitação: '))
    try:
        request = request_control.select(id)
    except KeyError:
        print('\nSolicitação não encontrada!')
    else:
        os.system('clear')
        request.show()

    input('[Enter] para continuar')


def del_request():
    os.system('clear')
    print('Remover Solicitação\n')

    id = int(input('ID da Solicitação: '))
    try:
        request_control.delete(id)
    except KeyError:
        print('\nSolicitação não encontrada!')
    else:
        print('\nSolicitação deletada')

    input('[Enter] para continuar')

