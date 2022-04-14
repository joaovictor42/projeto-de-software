from utils.ValidaFormulario import ValidaFormulario
from controle.ControleBanco import ConnEasyPayDB
from entidades.Usuario import Usuario


class ControleUsuario:

    def __init__(self):
        self.usuarios = []

    def adiciona_usuario(self, login, senha):
        if ValidaFormulario.login(login) and ValidaFormulario.senha(senha):
            novo_usuario = Usuario(login, senha)
            adiciona_usuario_sql = '''
                INSERT INTO USUARIOS (LOGIN, SENHA)
                VALUES (?, ?);
            '''
            self.usuarios.append(novo_usuario)
            ConnEasyPayDB.execute_sql(adiciona_usuario_sql, novo_usuario.collect())




