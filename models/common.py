
class DateConversion:
    def __init__(self, db_date):
        self.db_date = db_date
        self.day = self.db_date[-2:]
        months = {'00': '', '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março',
                  '04': 'Abril', '05': 'Maio', '06': 'Junho',
                  '07': 'Julho', '08': 'Agosto', '09': 'Setembro',
                  '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro'}
        self.month = self.db_date[5:7]
        self.month = months[self.month]
        self.year = self.db_date[0:4]

    def __str__(self):
        return f'{self.day} de {self.month} de {self.year}'