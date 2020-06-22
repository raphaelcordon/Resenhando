class Resenha:
    def __init__(self, id, tipo_review, author_id, spotify_link, nome_review,
                 nome_banda, review, date_register, image_file):
        self.id = id
        self.tipo_review = tipo_review
        self.author_id = author_id
        self.spotify_link = spotify_link
        self.nome_review = nome_review
        self.nome_banda = nome_banda
        self.review = review
        self.date_register = date_register
        self.image_file = image_file


class Users:
    def __init__(self, id, username, name, surname, password):
        self.id = id
        self.username = username
        self.name = name
        self.surname = surname
        self.password = password


class EditUsersPass:
    def __init__(self, id, password):
        self.id = id
        self.password = password