from util import validation

class InputField:

    def __init__(self, name, label, type=str, constraint=None) -> None:
        self.name = name
        self.label = label
        self.type = type
        self.constraint = constraint

    def validate(self, value) -> bool:
        if self.constraint is not None:
            return self.constraint(value)
        return True


name_field = InputField('name', 'Nome: ', constraint=validation.name)
email_field = InputField('email', 'Email: ', constraint=validation.email)
password_field = InputField('password', 'Senha: ', constraint=validation.password)
birth_field = InputField('birth', 'Data de Nascimento: ', constraint=validation.date)
pix_field = InputField('pix', 'Chave Pix: ', constraint=validation.pix)

