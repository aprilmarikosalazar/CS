"""Welcome to Step One."""


def main():
    """Prompt user for their name; then, greet them and state activity."""
    name = input("Please enter your name: ")
    first_string = "Hi "
    second_string = ", let's explore the void in your brain."
    complete_string = first_string + name + second_string
    print(complete_string)


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
