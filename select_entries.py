import pymysql


def translate_option_to_table(choice):
    print("SELECT 1")
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

    # I know the potential of sql injection threats, this would need to be controlled
    sql = f'SELECT * FROM {table};'

    cursor.execute(sql)
    selected_rows = cursor.fetchall()

    return selected_rows

def insert_rows(choice, data):
    table = translate_option_to_table(choice)

    conn = connect_to_db()
    cursor = conn.cursor()

    if (table == "troop"):
        sql = f"INSERT INTO troop (troop_name, troop_address, troop_website, troop_telephone_number)" \
            f"VALUES ('{data['name']}', '{data['address']}', '{data['website']}', '{data['phone']}');"
        print(sql)
    elif (table == "section"):
        sql = f"INSERT INTO section (section_name, section_type, meeting_day, meeting_start_time, meeting_end_time)" \
            f"VALUES ('{data['name']}', '{data['section_type']}', '{data['meeting_day']}', '{data['start_time']}', '{data['end_time']}');"
        print(sql)
    cursor.execute(sql)

    conn.commit()

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