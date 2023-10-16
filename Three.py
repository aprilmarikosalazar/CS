"""Next level. Move to Step Three."""


def main():
    """Prompt user for their name; then, greet them and state activity."""
    name = input("Please enter your name: ")
    print(f"Hi {name}, let's explore the void in your brain.")
    menu()


def menu():
    """Display Main Menu for user to select from."""
    print("Main Menu")
    print("1 - Load brain dataset one")
    print("2 - Load brain dataset two")
    print("3 - Compare average brain data")
    print("4 - Voids above threshold limit")
    print("5 - Highest void limit")
    print("6 - Change upper and lower bounds for dataset one")
    print("7 - Change upper and lower bounds for dataset two")
    print("9 - Quit")
    print_menu()


def print_menu():
    """Ask user for selection and provide appropriate output."""
    number = input("What is your choice? ")
    try:
        int_answer = int(number)
    except ValueError:
        print("Please enter a number only")
    else:

        if int_answer == 1:
            print("selection one is not functional yet")
        elif int_answer == 2:
            print("selection two is not functional yet")
        elif int_answer == 3:
            print("selection three is not functional yet")
        elif int_answer == 4:
            print("selection four is not functional yet")
        elif int_answer == 5:
            print("selection five is not functional yet")
        elif int_answer == 6:
            print("selection six is not functional yet")
        elif int_answer == 7:
            print("selection seven is not functional yet")
        elif int_answer == 9:
            print("selection nine is not functional yet")
        else:
            print("That wasn't a valid selection")


if __name__ == "__main__":
    main()
