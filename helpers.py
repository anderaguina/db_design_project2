
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