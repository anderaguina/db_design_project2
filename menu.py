def main_menu():

    # Give all the choices in a series of print statements.
    print("\n[1] LIST DATA")
    print("[2] INSERT DATA")
    
    
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    # Respond to the user's choice.
    if choice == '1':
        # sub_menu1()
        choice1 = select_menu()
        return choice, choice1

    if choice == '2':
        # sub_menu2()
        print("INSERT MENU")
        main_menu()

    elif choice == 'q':
        print("\nGoodbye.")
    else:
        print("\nI don't understand that choice, please try again.\n")
        main_menu()


def select_menu():
    print("\n[1] LIST TROOP DATA")
    print("\n[1] LIST SECTION DATA")
    print("\n[1] LIST YOUTH MEMBER DATA")
    print("\n[1] LIST ADULT VOLUNTEER DATA")
    print("\n[1] LIST NATIONAL EVENTS DATA")
    
    print("[b] Enter b to go back to main menu.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    return choice