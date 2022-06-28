from business.control.SystemControl import SystemControl
from view.pay_request import pay_request_view
from business.command.Processsing import Processing
import os


system = SystemControl()


def user_view():
    while True:
        os.system('clear')
        print('EasyPay - Usuário\n')
        print('1 - Solicitar Pagamento')
        print('2 - Histórico de Solicitações')
        print('3 - Histórico de Pagamentos')
        print('4 - Aguardar Processamento')
        print('0 - Logout\n')
        
        option = input('Opção: ')
        if option == '0':
            system.logout()
            return
        if option == '1':
            pay_request_view()
        elif option == '2':
            request_history()
        elif option == '3':
            payment_history()
        elif option == '4':
            Processing()
        else: 
            print('Opção Inválida')
            input('[Enter] para continuar')

def request_history():
    os.system('clear')
    print('Solicitações do Usuário\n')
    for request in system.request_control.requests:
        if request.target == system.session.user.expose():
            request.show()
    input('[Enter] para continuar')

def payment_history():
    os.system('clear')
    print('Pagamentos do Usuário\n')
    for payment in system.payment_control.payments:
        if payment.target == system.session.user.expose():
            payment.show()
    input('[Enter] para continuar')






