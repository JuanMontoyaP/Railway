import userinterface.ui as ui
from datahandling.filter import data_available
from functions.functions import unique_items_in_nested_list

import sys
from typing import List

def print_insert_main_page():
    """
    It prints the main page of the insert module
    
    - Returns: 
        - The user's selection
    """
    page = "Reports Page"
    description = "This page manages the reports"
    options = ["Actual state", "Make a prediction", "Select a certain curve"]
    zero_value = "Exit"
    ui.print_page(page, description, options, zero_value)
    return ui.page_selection(len(options))

def generates_make_predictions_options() -> List:
    """
    It returns a list of strings that are formatted as "Curve X, Y" where X is the curve number and Y is
    the thread number

    - Return: 
        - A list of strings.
    """
    records = unique_items_in_nested_list(data_available(["curve", "thread"]))
    return [f'Curve {record[0]}, {record[1]}' for record in records]

def print_make_predictions_page():
    page = "Predictions Page"
    description = "This page predicts when the rail is going to fail"
    options = generates_make_predictions_options()
    ui.print_page(page, description, options, "Exit")
    selection = ui.page_selection(len(options))
    if selection:
        pass
    else:
        sys.exit("Exit program")
    
def reports_page():
    selection = print_insert_main_page()
    if selection == 1:
        pass
    elif selection == 2:
        print_make_predictions_page()
    elif selection == 3:
        pass
    else:
        sys.exit("Exit program")

def main():
    pass

if __name__ == '__main__':
    main()