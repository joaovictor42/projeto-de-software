import os
from business.control.SessionControl import SessionControl
from business.control.RequestControl import RequestControl
from business.control.PaymentControl import PaymentControl
from business.control.ProcessingControl import process
from view.pay_request import pay_request_view

request_control = RequestControl()
payment_control = PaymentControl()
session = SessionControl()

def user_view():
    while True:
        os.system('clear')
        print('EasyPay - Usuário\n')
        print('1 - Solicitar Pagamento')
        print('2 - Histórico de Solicitações')
        print('3 - Histórico de Pagamentos')
        print('0 - Logout\n')
        
        option = input('Opção: ')
        if option == '0':
            session.logout
            return
        if option == '1':
            pay_request_view()
        elif option == '2':
            request_history()
        elif option == '3':
            pass
        elif option == '4':
            os.system('clear')
            process()
            print('Processamento Concluído!')
            input('[Enter] para continuar')
        else: 
            print('Opção Inválida')
            input('[Enter] para continuar')

def request_history():
    os.system('clear')
    print('Solicitações do Usuário\n')
    for request in request_control.requests:
        if request.target == session.user.expose():
            request.show()
    input('[Enter] para continuar')






