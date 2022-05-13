import userinterface.ui as ui
import reports.reports as rep
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
    options = ["Generate reports", "Make a prediction"]
    zero_value = "Exit"
    ui.print_page(page, description, options, zero_value)
    return ui.page_selection(len(options))

def unique_curves(keys) -> List:
    """
    It returns a list of strings that are formatted as "Curve X, Y" where X is the curve number and Y is
    the thread number

    - Return: 
        - A list of strings.
    """
    return unique_items_in_nested_list(data_available(keys))

def print_make_predictions_page():
    page = "Predictions Page"
    description = "This page predicts when the rail is going to fail"
    # options = unique_curves()
    options = [f'Curve {record[0]}, {record[1]}' for record in unique_curves(["curve", "thread"])]

    ui.print_page(page, description, options, "Exit")
    selection = ui.page_selection(len(options))
    if selection:
        pass
    else:
        sys.exit("Exit program")
    
def print_generate_reports_page():
    page = "Reports Page"
    description = "This generates the report for a certain curve"
    options = [f'Curve {record[0]}, {record[1]}, date {(record[2][:10])}' for record in unique_curves(["curve", "thread", "date"])]
    ui.print_page(page, description, options, "Exit")
    selection = ui.page_selection(len(options))
    if selection:
        rep.generate_reports(options[selection - 1])
    else:
        sys.exit("Exit program")

def reports_page():
    selection = print_insert_main_page()
    if selection == 1:
        print_generate_reports_page()
    elif selection == 2:
        print_make_predictions_page()
    else:
        sys.exit("Exit program")

def main():
    pass

if __name__ == '__main__':
    main()