from flask import session


class DateConversion:
    def __init__(self, db_date):
        self.db_date = db_date
        self.day = self.db_date[8:10]
        months = {'00': '', '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março',
                  '04': 'Abril', '05': 'Maio', '06': 'Junho',
                  '07': 'Julho', '08': 'Agosto', '09': 'Setembro',
                  '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
        self.month = self.db_date[5:7]
        self.month = months[self.month]
        self.year = self.db_date[0:4]

    def __str__(self):
        return f'{self.day} de {self.month} de {self.year}'


class KeepInSession:
    def __init__(self, artistId, nome_review, review):
        """
        :return: Feed temporary data from "nova_resenha" to be re-filled in case of error.
        """
        session['artistId'] = artistId
        session['nome_review'] = nome_review
        session['review'] = review


class CleanSession:
    def __init__(self):
        """
        :return: Cleaning the data from "nova_resenha" in Session after succeed.
        """
        session['nome_review'] = ''
        session['nome_banda'] = ''
        session['review'] = ''
        session['review'] = ''


class CleanLoginItens:
    def __init__(self):
        """
        :return: Cleaning the data in Session.
        """
        session['id'] = ''
        session['name'] = ''
        session['email'] = ''
        session['surname'] = ''
        session['access_level'] = ''
        session['nome_review'] = ''
        session['nome_banda'] = ''
        session['review'] = ''
