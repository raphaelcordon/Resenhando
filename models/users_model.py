
class Users:
    def __init__(self, id, name, surname, password, email, changepass, read_comment, read_like):
        self.id = id
        self.name = name
        self.surname = surname
        self.password = password
        self.email = email
        self.changepass = changepass
        self.read_comment = read_comment
        self.read_like = read_like


class UsersPass:
    def __init__(self, id, password):
        self.id = id
        self.password = password
