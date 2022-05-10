import userinterface.ui as ui

from datahandling.insert import insert_rail_data
from datahandling.filter import data_available

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
    """
    It takes the data from the user and inserts it into the database
    """
    os.system("cls")
    ui.print_headings("Insert New Data")
    insert_rail_data()
    print("Data loaded successfully!")

def show_available_data():
    """
    It prints out the available data in the database
    """
    keys = ["curve", "thread", "date","reprofiling"]
    records = data_available(keys)
    for record in records:
        print(f'Curve: {record[0]}, Thread: {record[1]}, Date: {record[2][:10]}, Reprofiling: {record[3]}')

def view_data_page():
    """
    It clears the screen, prints a heading, prints a description, and then calls a function to show the
    available data
    """
    os.system("cls")
    ui.print_headings("View Available Data")
    ui.print_description("This is the available data")
    show_available_data()

def insert_page():
    selection = print_insert_main_page()
    if selection == 1:
        insert_data_page()
    elif selection == 2:
        view_data_page()
    else:
        sys.exit("Exit program")