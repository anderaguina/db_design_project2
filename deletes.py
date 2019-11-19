from conn import connect_to_db
from helpers import translate_option_to_table


def delete_row(request_object):
    table = translate_option_to_table(request_object["choice1"])
    
    conn = connect_to_db()
    cursor = conn.cursor()

    target_id = request_object["id_target"]

    if (table == "troop"):
        sql = f"DELETE FROM troop WHERE troop_name = '{target_id}'"
    elif (table == "section"):
        sql = f"DELETE FROM section WHERE section_name = '{target_id}'"

    cursor.execute(sql)

    conn.commit()