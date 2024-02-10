# -*- coding:utf-8 -*-
import pymysql

from govstat import settings
from pymysql.cursors import DictCursor

if __name__ == '__main__':
    db_connect = pymysql.connect(
                host=settings.DB.get('HOST'),
                port=settings.DB.get('PORT'),
                user=settings.DB.get('USERNAME'),
                password=settings.DB.get('PASSWORD'),
                db=settings.DB.get('DATABASE'),
                charset=settings.DB.get('CHARSET'),
                cursorclass=pymysql.cursors.DictCursor
            )
    db_connect.ping()
    with db_connect.cursor() as cursor:
        # cursor.execute("truncate province")
        # cursor.execute("truncate city")
        cursor.execute("truncate county")
        # cursor.execute("truncate town")
        # cursor.execute("truncate village")
    db_connect.commit()

    print('Clear table province Success!')

