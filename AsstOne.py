""" This is my submission for Assignment One. """


def main():
    """ Prompt the user to enter their name, then greet them and state the
    activity.
    """
    name = input("Please enter your name: ")
    first_string = "Hi "
    second_string = ", let's explore some historical temperatures."
    complete_string = first_string + name + second_string
    print(complete_string)


if __name__ == "__main__":
    main()


"""
--- sample run #1 ---
Please enter your name: April
Hi April, let's explore some historical temperatures.

--- sample run #2 ---
Please enter your name: PyCharm
Hi PyCharm, let's explore some historical temperatures.
"""