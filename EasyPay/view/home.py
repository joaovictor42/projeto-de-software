from business.control.SystemControl import SystemControl
from view.admin import admin_view
from view.user import user_view
from util import login
import os

system = SystemControl()


def home_view():
    while True:
        os.system('clear')
        print('EasyPay - Login\n')

        email = input('Email: ')
        password = input('Senha: ') 

        authorized, id = login.verify(email, password)
        if not authorized:
            print('\nCredenciais inválidas')
            option = input('Continuar (S/N): ').upper()
            if option == 'S':
                continue
            else:
                return
        user = system.login(id)
        if user.admin:
            admin_view()
        else:
            user_view()

    


