import re
from business.control.UserControl import UserControl


def name(name: str) -> bool:
    constraint = r'^[\sa-zA-Z]{1,20}$'
    return re.match(constraint, name) is not None


def email(email: str) -> bool:
    constraint = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if re.match(constraint, email) is None:
        return False
    try:
        UserControl().select(email)
    except KeyError:
        return True
    return False


def password(password: str) -> bool:
    constraint = r'^((?=\S*?[a-zA-Z])(?=(?:\S*?[0-9]){2,})\w{8,20})$'
    return re.match(constraint, password) is not None


def date(date: str) -> bool:
    return True


def pix(pix: str) -> bool:
    return True


