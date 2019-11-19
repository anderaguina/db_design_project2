from menu import main_menu
from select_entries import select_rows
from inserts import insert_rows
from updates import update_row
from deletes import delete_row

if __name__ == "__main__":
    response = main_menu()

    # Depending on the option selected in the main menu and the type of table the user wants
    # to interact with, call different functions
    while response["choice"] != 'q':
        # Case select
        if response['choice'] == '1':
            if response['choice1'] != 'b':            
                results = select_rows(response['choice1'])
                for result in results:
                    print(result)

            response = main_menu()
        elif response['choice'] == '2':
            if response['choice1'] != 'b':
                insert_rows(response['choice1'], response['data'])
            response = main_menu()            
        elif response['choice'] == '3':
            if response['choice1'] != 'b':
                update_row(response)
            response = main_menu()
        elif response['choice'] == '4':
            if response['choice1'] != 'b':
                delete_row(response)
            response = main_menu()
        elif response['choice'] == 'q':
            print("\nGoodbye.")
        else:
            print("\nI don't understand that choice, please try again.\n")
            response = main_menu()
