import os
from business.control.SessionControl import SessionControl
from business.control.UserControl import UserControl
from util import login
from view.admin import admin_view
from view.user import user_view

session = SessionControl() 
user_control = UserControl()

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

        user = user_control.select(id)
        session.login(user)
        if user.admin:
            admin_view()
        else:
            user_view()

    


