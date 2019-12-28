# 新的数据库连接，有字段名称

import pymysql

class mysql_db(object):
    def __init__(self, host, port, user, passwd, db, print = print):
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.print = print

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.db, charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as result:
            self.print(result)
            self.print('connect mysql error.')

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()
            titles = []
            for field_desc in self.cursor.description:
                titles.append(field_desc[0])
            result = []
            for r in rows:
                result.append(dict(zip(titles, r)))
            return result
        except:
            self.print(sql + ' select failed.')
            return None

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except:
            self.print(sql + ' insert failed.')
            self.conn.rollback()
            return -1

    def insert_many(self, sql, val):
        try:
            self.cursor.executemany(sql, val)
            self.conn.commit()
            return 0
        except:
            self.print(sql + val + ' insert failed.')
            self.conn.rollback()
            return -1

    def update(self,sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return 0
        except Exception as result:
            self.print(result)
            self.print(sql + ' update failed.')
            self.conn.rollback()
            return -1


    def close(self):
        self.cursor.close()
        self.conn.close()
