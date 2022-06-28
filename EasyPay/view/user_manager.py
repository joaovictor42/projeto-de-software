import os
from business.model.User import User
from business.control.UserControl import UserControl
from business.control.SessionControl import SessionControl
from util.InputField import *

user_control = UserControl()
session = SessionControl()

def user_manager_view():
    while True:
        os.system('clear')
        print('Gerencimento de Usuários\n')
        print('1 - Listar Usuários (Nome)')
        print('2 - Listar Usuários (Idade)')
        print('3 - Visualizar Usuário')
        print('4 - Adicionar Usuário')
        print('5 - Alterar Usuário')
        print('6 - Deletar Usuário')
        print('0 - Voltar\n')

        option = input('Opção: ')
        if option == '0':
            return
        elif option == '1':
            user_control.list()
        elif option == '2':
            user_control.list_by_birth()
        elif option == '3':
            select_user()
        elif option == '4':
            create_user()
        elif option == '5':
            update_user()
        elif option == '6':
            del_user()
        else:
            print('Opção Inválida')
            input('[Enter] para continuar')


def select_user():
    os.system('clear')
    print('Selecionar Usuário\n')

    id = int(input('ID do Usuário: '))
    try:
        user = user_control.select(id)
    except KeyError:
        print('\nUsuário não encontrado!')
    else:
        os.system('clear')
        print('Informações do Usuário:\n')
        user.show()

    input('[Enter] para continuar')


def create_user():
    os.system('clear')
    print('Cadastrar Usuário\n')

    info = dict()
    fields = [
        name_field, email_field, password_field, 
        birth_field, pix_field  
    ]
    for field in fields:
        while True:
            value = input(field.label)
            if value:
                if field.validate(value):
                    info[field.name] = value
                    break
                else:
                    print('Valor inválido!')
            else:
                return

    new_user = User(**info) 
    user_control.insert(new_user)
    new_user.save()
    
    print('\nUsuário criado!')
    input('[Enter] para continuar')


def update_user():
    os.system('clear')
    print('Alterar Usuário\n')

    id = int(input('ID do Usuário: '))
    try:
        user = user_control.select(id)
    except KeyError:
        print('\nO usuário não existe!')
        input('[Enter] para continuar')
        return 

    updates = dict()
    fields = [
        name_field, email_field, password_field, 
        birth_field, pix_field  
    ]
    for field in fields:
        while True:
            value = input(field.label)
            if value:
                if field.validate(value):
                    updates[field.name] = value
                    break
                else:
                    print('Valor inválido!')
            else:
                break
    user_info = user.to_dict()
    user_info.update(updates)
    user_control.update(user.id, user_info)

    print('\nCadastro atualizado')
    input('[Enter] para continuar')


def del_user():
    os.system('clear')
    print('Deletar Usuário\n')

    id = int(input('ID do Usuário: '))
    try:
        user_control.delete(id)
    except KeyError:
        print('\nO usuário não existe!')
    else:
        print('\nUsuário deletado')

    input('[Enter] para continuar')
