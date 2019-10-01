"""
Application main menu.
"""

import sys

from dionysus_app.class_functions import create_classlist


def welcome_blurb() -> None:
    print("Welcome to Dionysus - student avatar graph generator\n")


def main_menu_options() -> None:
    print("Dionysus - Main menu\n")
    print("Please select an option by entering the corresponding number, and press return:\n"
          "     1. Create a classlist\n"
          "     2. Edit a classlist\n"
          "     3. Create a new graph\n"
          "     Enter Q to quit.\n")


def take_main_menu_input() -> None:
    """
    Takes input and runs chosen action.
    Flag for unselected/no option chosen used to exit the loop when chosen
    action finishes, returning to main menu run loop rather than option
    selection, which will reprint the menu options.

    :return: None
    """
    possible_options = {
        '1': create_classlist,
        '2': 'edit_classlist',
        '3': 'create_graph',
        'q': quit_app,
        'Q': quit_app,
    }
    unselected = True
    while unselected:
        chosen_option = input('>>> ')

        try:
            possible_options[chosen_option]()
            unselected = False  # Exiting the loop when chosen action finishes.
        except KeyError:
            print("Invalid input.")


def quit_app() -> None:
    sys.exit()


# Create a classlist
    # enter name and avatar file location

# Edit a class list
    # edit list entries
    # edit individual student data (eg name spelling, change image)


def run_main_menu() -> None:
    welcome_blurb()

    while True:
        main_menu_options()
        take_main_menu_input()
    quit_app()


if __name__ == "__main__":
    run_main_menu()
