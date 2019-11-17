import pymysql
from conn import connect_to_db
from helpers import translate_option_to_table


def select_rows(choice):
    table = translate_option_to_table(choice)
    conn = connect_to_db()
    cursor = conn.cursor()

    # I know the potential of sql injection threats, this would need to be controlled
    sql = f'SELECT * FROM {table};'

    cursor.execute(sql)
    selected_rows = cursor.fetchall()

    return selected_rows

def select_rows_filtering():
    pass
