import os
from business.control.SessionControl import SessionControl
from view.user_manager import user_manager_view
from view.pay_manager import pay_manager_view
from view.request_manager import request_manager_view
from business.report.HtmlReport import HtmlReport
from business.report.MdReport import MdReport


session = SessionControl()

def admin_view():
    while True:
        os.system('clear')
        print('EasyPay - Administrador\n')
        print('1 - Gerenciamento de Usuários')
        print('2 - Gerenciamento de Pagamentos')
        print('3 - Gerenciamento de Solicitações')
        print('4 - Export Relatório (HTML)')
        print('5 - Export Relatório (Markdown)')
        print('0 - Logout\n')

        option = input('Opção: ')
        if option == '0':
            session.logout()
            return
        elif option == '1':
            user_manager_view()
        elif option == '2':
            pay_manager_view()
        elif option == '3':
            request_manager_view()
        elif option == '4':
            HtmlReport().export('EasyPay-Report')
            os.system('clear')
            print('\nExportação Concluída\n')
            input('[Enter] para continuar')
        elif option == '5':
            MdReport().export('EasyPay-Report')
            os.system('clear')
            print('\nExportação Concluída\n')
            input('[Enter] para continuar')

        else:
            print('Opção Inválida')
            input('[Enter] para continuar')





