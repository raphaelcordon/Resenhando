import psycopg2


class PostgreDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='ec2-52-31-70-136.eu-west-1.compute.amazonaws.com',
            database='d37k7t1n9j0gnt',
            user='jsjtbbbgrlwylu',
            port='5432',
            password='fd7046128d574538515e2fb9a30347c56cbd6e50ada6a57f59b9c7dcd90b605f '
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
