from utils.ValidaFormulario import ValidaFormulario
from entidades.Usuario import Usuario


class ControleUsuario:

    def __init__(self):
        self.usuarios = []

    def adiciona_usuario(self, login, senha):
        if ValidaFormulario.login(login) and ValidaFormulario.senha(senha):
            novo_usuario = Usuario(login, senha)
            self.usuarios.append(novo_usuario)




