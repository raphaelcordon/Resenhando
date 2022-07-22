import psycopg2


class PostgreDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='ec2-52-211-37-76.eu-west-1.compute.amazonaws.com',
            database='d88297i13p6bf9',
            user='riqvbarhkhkheq',
            port='5432',
            password='46285b6fc9402d795c768d431d33eca11759b505a227596eb8a870cb9a137718'
        )
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def queryParams(self, query, params):
        self.cur.execute(query, params)
        self.conn.commit()

    def fetchOne(self):
        return self.cur.fetchone()

    def fetchAll(self):
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
