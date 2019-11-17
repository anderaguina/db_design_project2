from menu import main_menu
from select_entries import select_rows, insert_rows

if __name__ == "__main__":
    choice, choice1, data = main_menu()

    # Depending on the option selected in the main menu and the type of table the user wants
    # to interact with, call different functions
    while choice != 'q':
        print(f"Choice = {choice}")
        print(f"Choice1 = {choice1}")
        # Case select
        if choice == '1':
            if choice1 != 'b':            
                results = select_rows(choice1)
                for result in results:
                    print(result)

            choice, choice1, data = main_menu()
        elif choice == '2':
            if choice1 != 'b':
                insert_rows(choice1, data)
            choice, choice1, data = main_menu()
            
        elif choice == '3':
            choice, choice1, data = main_menu()
        elif choice == '4':
            choice, choice1, data = main_menu()
        elif choice == '5':
            choice, choice1, data = main_menu()
        elif choice == 'q':
            print("\nGoodbye.")
        else:
            print("\nI don't understand that choice, please try again.\n")
            choices = main_menu()
