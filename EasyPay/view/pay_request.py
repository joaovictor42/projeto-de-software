import os
from infra.factory.RequestFactory import *
from business.control.RequestControl import RequestControl

request_control = RequestControl()

def pay_request_view():
    while True:
        os.system('clear')
        print('Solicitação de Pagamentos\n')
        print('1 - Cartão de Crédito')
        print('2 - Cartão de Débito')
        print('3 - Pix')
        print('0 - Voltar\n')

        option = input('Opção: ')
        if option == '0':
            return
        if option == '1':
            credit_card_view()
        elif option == '2':
            debit_card_view()
        elif option == '3':
            pix_view()
        else: 
            print('Opção Inválida')
            input('[Enter] para continuar')


def credit_card_view():
    os.system('clear')
    print('Cartão de Crédito\n')

    request = dict()
    request['purchase']      = input('Valor da Compra: ')
    request['name']          = input('Titular: ')
    request['card_number']   = input('Número: ')
    request['security_code'] = input('Código: ')
    request['expiry']        = input('Validade: ')
    request['flag']          = input('Bandeira: ')

    new_request = CreditCardRequestCreator.factory(request)
    request_control.insert(new_request)

    print('\nSolicitação em análise...')
    input('[Enter] para continuar')


def debit_card_view():
    os.system('clear')
    print('Cartão de Débito\n')

    request = dict()
    request['purchase']      = input('Valor da Compra: ')
    request['name']          = input('Titular: ')
    request['card_number']   = input('Número: ')
    request['security_code'] = input('Código: ')
    request['expiry']        = input('Validade: ')
    request['flag']          = input('Bandeira: ')

    new_request = DebitCardRequestCreator.factory(request)
    request_control.insert(new_request)

    print('\nSolicitação em análise...')
    input('[Enter] para continuar')


def pix_view():
    os.system('clear')
    print('Pix\n')

    name = input('Comprador: ')
    purchase = float(input('Valor da Compra: '))
    new_request = PixRequestCreator.factory(name, purchase)
    request_control.insert(new_request)

    print(f'Código Pix: {new_request.code}\n')
    input('[Enter] para continuar')


