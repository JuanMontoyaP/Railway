import userinterface.ui as ui

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

def reports_page():
    selection = print_insert_main_page()

def main():
    pass

if __name__ == '__main__':
    main()