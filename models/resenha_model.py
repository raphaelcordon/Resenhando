
class Resenha:
    def __init__(self, id, tipo_review, author_id, nome_review, spotify_id, review, date_register, genre):
        self.id = id
        self.tipo_review = tipo_review
        self.author_id = author_id
        self.nome_review = nome_review
        self.spotify_id = spotify_id
        self.review = review
        self.date_register = date_register
        self.genre = genre


class ResenhaAuthorId:
    def __init__(self, id):
        self.id = id