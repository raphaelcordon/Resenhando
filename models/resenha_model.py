
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

class ResenhaCapa:
    def __init__(self, capa):
        self.capa = capa