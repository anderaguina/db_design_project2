def main_menu():

    # Give all the choices in a series of print statements.
    print("\n[1] LIST DATA")
    print("[2] INSERT DATA")
    
    
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    # Respond to the user's choice.
    if choice == '1':
        choice1 = select_menu()
        return choice, choice1, "no data"

    if choice == '2':
        # sub_menu2()
        choice1, data = insert_menu()
        print(f"INSERT MENU: {choice}, {choice1}, {data}")
        return choice, choice1, data

    elif choice == 'q':
        print("\nGoodbye.")
        return choice
    else:
        print("\nI don't understand that choice, please try again.\n")
        main_menu()


def select_menu():
    print("\n[1] LIST TROOP DATA")
    print("\n[2] LIST SECTION DATA")
    print("\n[3] LIST YOUTH MEMBER DATA")
    print("\n[4] LIST ADULT VOLUNTEER DATA")
    print("\n[5] LIST NATIONAL EVENTS DATA")
    
    print("[b] Enter b to go back to main menu.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    return choice

def insert_menu():
    print("\n[1] CREATE NEW TROOP")
    print("\n[2] CREATE NEW SECTION")
    
    print("[b] Enter b to go back to main menu.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    if choice == '1':
        data = request_troop_data()
    elif choice == '2':
        data = request_section_data()
        print("choice2")

    return choice, data

def request_troop_data():
    name = input("\nName of the troop? ")
    address = input("\nAddress of the troop? ")
    website = input("\nWebsite of the troop? ")
    phone = input("\nPhone number of the troop? ")

    troop = {
        "name": name,
        "address": address,
        "website": website,
        "phone": phone
    }

    return troop

def request_section_data():
    name = input("\nName of the section? ")
    section_type = input("\nSection type? ")
    meeting_day = input("\nEnter meeting day ")
    start_time = input("\nEnter meeting start time ")
    end_time = input("\nEnter meeting ending time ")

    section = {
        "name": name,
        "section_type": section_type,
        "meeting_day": meeting_day,
        "start_time": start_time,
        "end_time": end_time
    }

    return section

