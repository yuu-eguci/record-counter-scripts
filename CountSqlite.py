
"""Record Counter for Sqlite

""" 

import sqlite3
from contextlib import closing
from pprint import pprint


def count_tables(dbname):

    # 接続します。
    with closing(sqlite3.connect(dbname)) as con:

        # おやくそく。
        con.row_factory = sqlite3.Row

        # テーブル一覧取得します。
        sql = ' '.join([
            'SELECT',
                'tbl_name',
            'FROM sqlite_master',
            'WHERE type=:type',
            'ORDER BY tbl_name',
        ])
        bind = { 'type': 'table', }
        dic = {dict(row)['tbl_name']:0 for row in con.execute(sql, bind)}

        # 各テーブルに count をかけます。
        for table_name in dic:
            sql = ' '.join([
                'SELECT',
                    'COUNT(0) count',
                f'FROM {table_name}',
            ])
            dic[table_name] = con.execute(sql).fetchone()['count']

    return dic


if __name__ == '__main__':
    pprint(count_tables('test.sqlite3'))
