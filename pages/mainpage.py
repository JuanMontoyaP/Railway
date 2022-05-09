import userinterface.ui as ui

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
    ui.print_page(page, description, options, zero_value)
    return ui.page_selection(len(options))
    
def main():
    main_page()

if __name__ == '__main__':
    main()