import os
from business.control.SessionControl import SessionControl
from business.control.RequestControl import RequestControl
from business.control.PaymentControl import PaymentControl
from business.control.StatsControl import StatsControl
from business.control.ProcessingControl import process
from view.pay_request import pay_request_view

request_control = RequestControl()
payment_control = PaymentControl()
stats_control = StatsControl()
session = SessionControl()

def user_view():
    while True:
        os.system('clear')
        print('EasyPay - Usuário\n')
        print('1 - Solicitar Pagamento')
        print('2 - Histórico de Solicitações')
        print('3 - Histórico de Pagamentos')
        print('4 - Aguardar Processamento')
        print('5 - Stats')
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
            payment_history()
        elif option == '4':
            os.system('clear')
            process()
            print('Processamento Concluído!')
            input('[Enter] para continuar')
        elif option == '5':
            print(stats_control.snapshot())
            input()
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

def payment_history():
    os.system('clear')
    print('Pagamentos do Usuário\n')
    for payment in payment_control.payments:
        if payment.target == session.user.expose():
            payment.show()
    input('[Enter] para continuar')






