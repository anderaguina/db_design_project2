from conn import connect_to_db
from helpers import translate_option_to_table

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