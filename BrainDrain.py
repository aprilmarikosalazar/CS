"""You have entered the void. Welcome."""


def main():
    """Prompt user for their name; then, greet them and state activity."""
    name = input("Please enter your name: ")
    print(f"Hi {name}, let's explore the void in your brain.")
    menu()


def menu():
    """Display Main Menu for user to select from."""
    print("Main Menu")
    print("1 - Load data of brain scan one")
    print("2 - Load data of brain scan two")
    print("3 - Fast Fourier transformation")
    print("4 - Values of Fourier transformation")
    print("5 - Excitation samples in k-space")
    print("6 - Decaying exponential for Lorentzian line")
    print("7 - Contrast-to-noise ratio")
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




"""
--- sample run #1 ---
Please enter your name: April
Hi April, let's explore the void in your brain.

--- sample run #2 ---
Please enter your name: Makima
Hi Makima, let's explore the void in your brain.
"""
