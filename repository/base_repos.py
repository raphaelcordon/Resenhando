import psycopg2


class PostgreDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='cdju6b3s1cdqa9.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com',
            database='d16lga7geo7bjv',
            user='u96inmogjs8uii',
            port='5432',
            password='p65de7c2f3f380da6d6bdbe9cb96b5311e8fdfbc1478f521ab10077cafc15d6f2'
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
