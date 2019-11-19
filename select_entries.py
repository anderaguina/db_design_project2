import pymysql
from conn import connect_to_db
from helpers import translate_option_to_table


def select_rows(choice):
    table = translate_option_to_table(choice)

    # I know the potential of sql injection threats, this would need to be controlled
    if (choice == "3"):
        troop = input("\nEnter name of the troop please: ")
        sql = f'SELECT * FROM section WHERE troop_name = "{troop}";'
    elif (choice == "5"):
        troop = input("\nEnter name of the troop please: ")
        sql = f'SELECT * FROM volunteer WHERE troop_name = "{troop}";'
    elif (choice == "7"):
        section = input("\nEnter name of the section please: ")
        sql = f'SELECT * FROM member WHERE section_name = "{section}";'
    elif (choice == "9"):
        event = input("\nEnter id of the event please: ")
        sql = f'SELECT * FROM member_attends_event WHERE event_id = "{event}";'
    else:
        sql = f'SELECT * FROM {table};'

    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute(sql)
    selected_rows = cursor.fetchall()

    return selected_rows

def select_rows_filtering():
    pass
