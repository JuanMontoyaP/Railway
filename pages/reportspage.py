import userinterface.ui as ui
from datahandling.filter import data_available

import sys

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

def print_make_predictions_page():
    page = "Predictions Page"
    description = "This page predicts when the rail is going to fail"
    options = data_available(["curve", "thread"])
    ui.print_page(page, description)
    print(options)

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