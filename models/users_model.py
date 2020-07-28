
class Users:
    def __init__(self, id, name, surname, password, email, changepass):
        self.id = id
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.changepass = changepass


class UsersPass:
    def __init__(self, id, password):
        self.id = id
        self.password = password
