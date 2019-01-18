"""UI elements for class_functions"""
from dionysus_app.class_registry_functions import classlist_exists
from dionysus_app.UI_menus.UI_functions import (clean_for_filename,
                                                input_is_essentially_blank,
                                                select_file_dialogue,
                                                )


def take_classlist_name_input():
    """
    Prompts user for classlist name.
    It repeats until user provide correct classlist name.

    :return: str
    """

    while True:
        classlist_name = input('Please enter a name for the class: ')

        if input_is_essentially_blank(classlist_name):  # blank input
            continue

        classlist_name = clean_for_filename(classlist_name)
        if classlist_exists(classlist_name):
            print('A class with this name already exists.')
            continue
        break
    return classlist_name


def take_student_name_input(class_data):
    """
    Prompts user for student name.

    :param class_data: str
    :return: str
    """
    while True:
        student_name = input("Enter student name, or 'end', and hit enter: ")
        if input_is_essentially_blank(student_name):  # Do not allow blank input
            print('Please enter a valid student name.')
            continue

        if student_name in class_data:
            print("This student is already a member of the class.")
            continue
        return student_name


def blank_class_dialogue():
    while True:
        choice = input("Do you want to create an empty class? y/n")
        if choice.upper() == 'Y':
            return True
        if choice.upper() == 'N':
            return False
        # TODO: Option to cancel creation here/after entering a class name (eg made typo in class name)
        print('Please enter y for yes to create empty class, or n to return to student input.')


def class_data_feedback(classlist_name: str, class_data_dict: dict):
    """
    Print classlist name and list of students as user feedback.

    :param classlist_name: str
    :param class_data_dict: dict
    :return: None
    """
    print(f'\nClass name: {classlist_name}')
    if not class_data_dict:
        print("No students entered.")
    else:
        for key in class_data_dict:
            print(key)


def display_class_selection_menu(class_options: dict):
    """
    Print "Select class from list:" followed by numbered option list.

    :param class_options: dict
    :return: None
    """
    print("Select class from list:")
    for key, class_name in class_options.items():
        print(f'{key}. {class_name}')


def take_class_selection(class_options):
    unselected = True
    selected_class = None
    while unselected:
        chosen_option = input('Select class: ')

        try:
            selected_class = class_options[chosen_option]
            unselected = False  # Exiting the loop when chosen action finishes.
        except KeyError:
            print("Invalid input.\n"
                  "Please enter the integer beside the name of the desired class.")

    return selected_class


def display_student_selection_menu(student_list_dict: dict):
    """
    Print "Select student from list:" followed by numbered option list.

    :param student_list_dict: dict
    :return: None
    """
    print("Select student from list:")
    for key, class_name in student_list_dict.items():
        print(f'{key}. {class_name}')


def select_avatar_file_dialogue():
    """
    Prompts user to select an avatar file. Only displays PNG files.
    :return: str or None
    """
    dialogue_box_title = 'Select .png format avatar:'
    filetypes = [('.png files', '*.png'), ("all files", "*.*")]
    start_dir = '..'  # start at parent to app directory.

    filename = select_file_dialogue(dialogue_box_title, filetypes, start_dir)

    return filename