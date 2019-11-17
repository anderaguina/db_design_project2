import pymysql


def translate_option_to_table(choice):

    if choice == "1":
        table = "troop"
    elif choice == "2":
        table = "section"
    elif choice == "3":
        table = "youth_bember"
    elif choice == "4":
        table = "adult_volunteer"
    elif choice == "5":
        table = "national_events"

    return table

def select_rows(choice):
    table = translate_option_to_table(choice)
    conn = connect_to_db()
    cursor = conn.cursor()

    sql = f'SELECT * FROM {table};'

    cursor.execute(sql)

    selected_rows = cursor.fetchall()

    return selected_rows()
    

def connect_to_db():
    try:
    # Open a database connection
        #connection = pymysql.connect( host = 'localhost', user = 'postgres', password = 'postgres', database = 'db_design_project2')
        
        connection = pymysql.connect(
            host='localhost',
            user='phpmyadmin',
            passwd='123',
            db='db_design_project2'
        )
        
        print("CONNECTED")
        return connection
    except:
        print("An exception occurred")