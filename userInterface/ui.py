import functions.functions as func

import os
from typing import List

def print_headings(heading: str):
    """
    This function prints a heading in the console
    
    - params 
        - heading [str]: The heading to be printed
    """
    msg = "Metro Analysis Proram"
    func.print_line()
    func.print_message(msg.center(70, " "))
    func.print_line()
    print()
    func.print_message(heading.upper().center(70))

def print_description(description: str):
    """
    It prints a centered string with the description of the page
    
    - params
        - description [Str]: The description of the page
    """
    func.print_message(description.center(70, "-"))
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

def print_page(page_name: str, description: str, options: List[str], zero_value: str):
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

def page_selection(options: int):
    """
    Reads the user selection of the page and validates that it is a valid selection
    
    - Params 
        - options [int]: Amount of values available to the user

    - Returns 
        - The selection of the user
    """

    while True:
        selection = input("Select and alternative:")
        try:
            selection = int(selection)
            if selection <=options:
                break
            else:
                raise ValueError
        except ValueError:
            print("Insert a valid option")
            pass
    return selection
    
def main():
    pass

if __name__ == '__main__':
    main()