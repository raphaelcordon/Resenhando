import psycopg2


class PostgreDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host='ec2-176-34-123-50.eu-west-1.compute.amazonaws.com',
            database='dgs1bk31h45p3',
            user='jrqbypzwfthnnb',
            port='5432',
            password='581cf159c1fb3d57e39bb6fc3238e9c92cce2574c6d0e5435eb87b06d2a8137a'
        )
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)
        self.conn.commit()

    def fetchOne(self):
        return self.cur.fetchone()

    def fetchAll(self):
        return self.cur.fetchall()

    def close(self):
        self.cur.close()
        self.conn.close()
