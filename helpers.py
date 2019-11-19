
def translate_option_to_table(choice):
    print("SELECT 1")
    if choice == "1":
        table = "troop"
    elif choice == "2":
        table = "section"
    elif choice == "3":
        table = "member"
    elif choice == "4":
        table = "volunteer"
    elif choice == "5":
        table = "national_events"
    elif choice == "6":
        table = "section_type"
    elif choice == "7":
        table = "member_attends_event"
    elif choice == "8":
        table = "event_is_organized_for_section_type"


    return table