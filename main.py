from menu import main_menu
from select_entries import select_rows


if __name__ == "__main__":
    choices = main_menu()

    print(f"choices = {choices}")

    if choices[0] == '1':
        print("HERE1")
        results = select_rows(choices[1])
        for result in results:
            print(result)
