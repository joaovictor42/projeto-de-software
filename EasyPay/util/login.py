from business.control.UserControl import UserControl

def verify(email, password):
    for user in UserControl().users:
        if user.email == email:
            return user.password == password, user.id
    return False, -1

    