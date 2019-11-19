import pymysql
from conn import connect_to_db
from helpers import translate_option_to_table


def select_rows(choice):
    table = translate_option_to_table(choice)

    # I know the potential of sql injection threats, this would need to be controlled
    if (choice == "3"):
        troop = input("\nEnter name of troop please: ")
        sql = f'SELECT * FROM section WHERE troop_name = "{troop}";'
    elif (choice == "5"):
        pass
    elif (choice == "7"):
        pass
    elif (choice == "9"):
        pass
    else:
        sql = f'SELECT * FROM {table};'

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(sql)
    selected_rows = cursor.fetchall()

    return selected_rows

def select_rows_filtering():
    pass
