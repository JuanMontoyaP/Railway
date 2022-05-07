from turtle import st
from functions import *

import os
from typing import List

def print_headings(heading: str):
    """
    This function prints a heading in the console
    
    - params 
        - heading [str]: The heading to be printed
    """
    msg = "Metro Analysis Proram"
    print_line()
    print_message(msg.center(70, " "))
    print_line()
    print()
    print_message(heading.upper().center(70))

def print_description(description: str):
    """
    It prints a centered string with the description of the page
    
    - params
        - description [Str]: The description of the page
    """
    print_message(description.center(70, "-"))
    print()

def print_options_of_the_page(options: List[str], zero_value: str):
    """
    It prints the options of the page
    
    - params 
        - options List[str]: Options of the page
        - zero_value [str]: The zero value of the page
    """
    for ind, option in enumerate(options):
        print("[{}]: {}".format(ind+1, option))
    print("[0]: {}".format(zero_value))

def print_page(page_name: str, description: str, options: List[str], zero_value: str) -> int:
    """
    It prints a page with a name, a description and a list of options, and returns the selected option
    
    - params: 
        - page_name [str]: The name of the page
        - description [str]: The description of the page
        - options List[str]: Options of the page
        - zero_value [str]: Zero value for the page

    - return: 
        - selection [int]: The selection of the user.
    """
    os.system('cls')
    print_headings(page_name)
    print_description(description)
    print_options_of_the_page(options, zero_value)

    while True:
        selection = input("Select and alternative:")
        try:
            selection = int(selection)
            if selection <=len(options):
                break
            else:
                raise ValueError
        except ValueError:
            print("Insert a valid option")
            pass
    return selection

def main_page():
    """
    It prints a page with a title, a description, and a list of options
    
    - returns: 
        - the result of the print_page function.
    """
    page = "Main Page"
    description = "This program collects data form CAT system and generates reports"
    options = ["Insert new data", "Generate reports"]
    zero_value = "Exit"
    return print_page(page, description, options, zero_value)
    
def main():
    main_page()


if __name__ == '__main__':
    main()