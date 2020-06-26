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

class DateConversion:
    def __init__(self, db_date):
        self.db_date = db_date
        self.day = self.db_date[-2:]
        months={'00': '', '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março',
                '04': 'Abril', '05': 'Maio', '06': 'Junho',
                 '07': 'Julho', '08': 'Agosto', '09': 'Setembro',
                 '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
        self.month = self.db_date[5:7]
        self.month = months[self.month]
        self.year = self.db_date[0:4]

    def __str__(self):
        return f'{self.day} de {self.month} de {self.year}'


class TranslateCapa:
    def __init__(self, capa):
        self.capa = capa