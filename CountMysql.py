
"""Record Counter for Mysql

"""

import pymysql.cursors
import re
from pprint import pprint


class TablesCounter:
    """全テーブルの Count を表示します。
       アレだぜ、そもそも InnoDB が正確な値を出してくれればよかったんだけどな。"""

    def __init__(self, db_settings):
        self.connection = pymysql.connect(
            host     = db_settings['host'],
            user     = db_settings['user'],
            password = db_settings['password'],
            db       = db_settings['db'],
            charset  = db_settings['charset'],
            cursorclass = pymysql.cursors.DictCursor)
        self.db_settings = db_settings


    def count_tables(self):
        """Top level method."""

        return {table:self.get_count(table) for table in self.get_tables()}


    def get_tables(self):
        """Get table names list."""

        with self.connection.cursor() as cursor:
            cursor.execute('SHOW TABLES')
            rows = cursor.fetchall()
        
        # こういう形式になってるからテーブル名だけにするよ。
        # [{'Tables_in_mashiro-db': 'account'},
        #  {'Tables_in_mashiro-db': 'authorizedip'},]
        for row in rows:
            yield list(row.values())[0]


    def get_count(self, table):
        """Returns the count of received table."""

        with self.connection.cursor() as cursor:
            cursor.execute(f'SELECT COUNT(0) count FROM {table}')
            row = cursor.fetchone()

        return row['count']


if __name__ == '__main__':

    db_settings = {
        'host'     : '',
        'user'     : '',
        'password' : '',
        'db'       : '',
        'charset'  : 'utf8',
    }
    counter = TablesCounter(db_settings)
    pprint(counter.count_tables())
