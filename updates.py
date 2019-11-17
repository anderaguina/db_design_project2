from conn import connect_to_db
from helpers import translate_option_to_table


def update_row(request_object):
    table = translate_option_to_table(request_object["choice1"])

    conn = connect_to_db()
    cursor = conn.cursor()

    data = request_object["data"]
    target_id = request_object["id_target"]

    if (table == "troop"):
        name = data["name"]
        address = data["address"]
        website = data["website"]
        phone = data["phone"]

        sql = f"UPDATE troop SET troop_name = '{name}', troop_address = '{address}'," \
            f"troop_website = '{website}', troop_telephone_number = '{phone}' WHERE troop_name = '{target_id}';"
        print(sql)
    elif (table == "section"):

        name = data["name"]
        section_type = data["section_type"]
        meeting_day = data["meeting_day"]
        start_time = data["start_time"]
        end_time = data["end_time"]

        sql = f"UPDATE section SET section_name = '{name}', section_type = '{section_type}'," \
            f"meeting_day = '{meeting_day}', meeting_start_time = '{start_time}', meeting_end_time = '{end_time}' WHERE section_name = '{target_id}';"
        print(sql)
    cursor.execute(sql)

    conn.commit()