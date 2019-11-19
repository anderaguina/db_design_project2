def main_menu():

    # Give all the choices in a series of print statements.
    print("\n[1] LIST DATA")
    print("\n[2] INSERT DATA")
    print("\n[3] UPDATE DATA")

    
    
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    # Respond to the user's choice.
    if choice == '1':
        choice1 = select_menu()
        response = {
            "choice": choice,
            "choice1": choice1
        }
        return response

    if choice == '2':
        # sub_menu2()
        choice1, data = insert_menu()
        print(f"INSERT MENU: {choice}, {choice1}, {data}")
        response = {
            "choice": choice,
            "choice1": choice1,
            "data": data
        }
        return response
    if choice == '3':
        # sub_menu2()
        choice1, id_target, data = update_menu()
        response = {
            "choice": choice,
            "choice1": choice1,
            "id_target": id_target,
            "data": data
        }
        return response

    elif choice == 'q':
        print("\nGoodbye.")
        response = {
            "choice": choice
        }
        return response
    else:
        print("\nI don't understand that choice, please try again.\n")
        main_menu()


def select_menu():
    print("\n[1] LIST TROOPS")
    print("\n[2] LIST SECTIONS")
    print("\n[3] LIST YOUTH MEMBERS")
    print("\n[4] LIST ADULT VOLUNTEERS")
    print("\n[5] LIST NATIONAL EVENTS")
    print("\n[6] LIST SECTION TYPES")
    print("\n[7] LIST MEMBERS ATTENDING NATIONAL EVENTS")
    print("\n[8] LIST NATIONAL EVENTS ORGANIZED FOR SECTION TYPES")
    
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

def update_menu():
    print("\n[1] TO UPDATE TROOP")
    print("\n[2] TO UPDATE SECTION")
    
    print("[b] Enter b to go back to main menu.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    id_entry = request_target_entry()

    if choice == '1':
        data = request_troop_data()

    elif choice == '2':
        data = request_section_data()

    return choice, id_entry, data

def request_target_entry():
    id_entry = input("\nPlease enter id of the entry to be updated ")
    return id_entry


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

