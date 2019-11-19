def main_menu():
    print("\n############## MAIN MENU ##############")
    # Give all the choices in a series of print statements.
    print("\n[1] LIST DATA")
    print("\n[2] INSERT DATA")
    print("\n[3] UPDATE DATA")
    print("\n[4] DELETE DATA")

    
    
    print("[q] Enter q to quit.")

    print("\n#######################################")

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
    if choice == '4':
        # sub_menu2()
        choice1, id_target = delete_menu()
        response = {
            "choice": choice,
            "choice1": choice1,
            "id_target": id_target
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
    print("\n############## SELECT MENU ##############")

    print("\n[1] LIST ALL TROOPS")
    print("\n[2] LIST ALL SECTIONS")
    print("\n[3] LIST ALL SECTIONS OF A TROOP")
    print("\n[4] LIST ALL ADULT VOLUNTEERS")
    print("\n[5] LIST ALL ADULT VOLUNTEERS OF A TROOP")
    print("\n[6] LIST ALL YOUTH MEMBERS")
    print("\n[7] LIST ALL YOUTH MEMBERS OF A SECTION")
    print("\n[8] LIST ALL NATIONAL EVENTS")
    print("\n[9] LIST ALL MEMBERS BOOKED TO ATTEND A NATIONAL EVENT")
    
    print("[b] Enter b to go back to main menu.")

    print("\n#########################################")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    return choice

def insert_menu():
    print("\n############## INSERT MENU ##############")

    print("\n[1] CREATE NEW TROOP")
    print("\n[2] CREATE NEW SECTION")
    
    print("[b] Enter b to go back to main menu.")

    print("\n#########################################")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    if choice == '1':
        data = request_troop_data()
    elif choice == '2':
        data = request_section_data()
        print("choice2")
    elif choice == 'b':
        return choice, "no data"
    else:
        print("\nI don't understand that choice, please try again.\n")
        insert_menu()

    return choice, data

def update_menu():
    print("\n############## UPDATE MENU ##############")
    
    print("\n[1] TO UPDATE TROOP")
    print("\n[2] TO UPDATE SECTION")
    
    print("[b] Enter b to go back to main menu.")

    print("\n#########################################")
    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    if choice == 'b':
        return choice, "no entry", "no data"

    id_entry = request_target_entry()

    if choice == '1':
        data = request_troop_data()

    elif choice == '2':
        data = request_section_data()
    else:
        print("\nI don't understand that choice, please try again.\n")
        update_menu()

    return choice, id_entry, data

def delete_menu():
    print("\n############## DELETE MENU ##############")

    print("\n[1] TO DELETE TROOP")
    print("\n[2] TO DELETE SECTION")
    
    print("[b] Enter b to go back to main menu.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    print("\n#########################################")
    if choice == 'b':
        return choice, "no entry"
    elif (choice != "1" and choice !="2"):
        print("\nI don't understand that choice, please try again.\n")
        delete_menu()

    id_entry = request_target_entry()
    
    return choice, id_entry

def request_target_entry():
    id_entry = input("\nPlease enter id of the entry to be affected ")
    return id_entry


def request_troop_data():
    name = input("\nEnter name of the troop: ")
    address = input("\nEnter address of the troop: ")
    website = input("\nEnter website of the troop: ")
    phone = input("\nEnter phone number of the troop: ")

    troop = {
        "name": name,
        "address": address,
        "website": website,
        "phone": phone
    }

    return troop

def request_section_data():
    name = input("\nEnter name of the section: ")
    section_type = input("\nEnter section type: ")
    meeting_day = input("\nEnter meeting day: ")
    start_time = input("\nEnter meeting start time: ")
    end_time = input("\nEnter meeting ending time: ")
    volunteer = input("\nEnter volunteer id of the section leader: ")
    troop = input("\nEnter name of troop to which the section will belong: ")

    section = {
        "name": name,
        "section_type": section_type,
        "meeting_day": meeting_day,
        "start_time": start_time,
        "end_time": end_time,
        "volunteer_id": volunteer,
        "troop_name": troop
    }

    return section

