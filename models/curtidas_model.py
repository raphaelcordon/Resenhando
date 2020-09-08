
class Curtidas:
    def __init__(self, id, user_id, resenha_id, login_date):
        self.id = id
        self.user_id = user_id
        self.resenha_id = resenha_id
        self.login_date = login_date


class CurtidasCount:
    def __init__(self, count):
        self.count = count