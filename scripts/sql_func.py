import scripts.db_conn as db_conn
from datetime import datetime,timedelta
import logging

logging.basicConfig(filename='docs/sql.log',level=logging.DEBUG)
log = logging.info
        
def sql_query(arg1,arg2):
    conn = db_conn.connect()
    cur = conn.cursor()

    query =(
        f"""SELECT [example] FROM [db.TABLE] WHERE {arg1} LIKE '{arg2}%'"""
    )

    cur.execute(query)
    result = cur.fetchall()

    if len(result) > 0:        
        print(f'success!\n\n{result}\n')
        log(f'sql query executed on {datetime.now()}:\n{result}\n')

    else:
        print('query returned no results')
