import userinterface.ui as ui

from datahandling.insert_data import insert_rail_data

import os
import sys

def print_insert_main_page():
    """
    It prints the main page of the insert module
    
    - Returns: 
        - The user's selection
    """
    page = "Insert Page"
    description = "This page manages the data"
    options = ["Insert new data", "View available data"]
    zero_value = "Exit"
    ui.print_page(page, description, options, zero_value)
    return ui.page_selection(len(options))

def insert_data_page():
    os.system("cls")
    ui.print_headings("Insert New Data")
    insert_rail_data()
    print("Data loaded successfully!")

def insert_page():
    selection = print_insert_main_page()
    if selection == 1:
        insert_data_page()