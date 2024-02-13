# -*- coding:utf-8 -*-
from govstat.settings import DB, BASE_DIR
from govstat.database import DbManager

if __name__ == '__main__':
    db_manager = DbManager(DB)
    connection = db_manager.connection
    connection.ping()

    with connection.cursor() as cursor:
        cursor.execute("truncate province")
        cursor.execute("truncate city")
        cursor.execute("truncate county")
        cursor.execute("truncate town")
        cursor.execute("truncate village")

    connection.commit()
    db_manager.close()
    print('Clear table province Success!')

