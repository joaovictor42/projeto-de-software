

class ValidaFormulario:

    @staticmethod
    def login(login):
        if login.isalpha() and 0 < len(login) <= 12:
            return True
        return False

    @staticmethod
    def senha(senha):
        if senha.isalnum() and num_count(senha) >= 2 and 8 <= len(senha) <= 20:
            return True
        return False    
        
def num_count(string):
    count = 0
    for char in string:
        if char.isnumeric():
            count += 1
    return count       
