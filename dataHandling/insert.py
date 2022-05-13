import functions.functions as func
from .write import write_a_dictionary_in_a_json_file
from .read import choose_a_file

from typing import List
from datetime import datetime

def valid_input(user_input: str, valid_options: List[str]):
    """
    It takes a string and a list of strings as input, and returns the string if it's in the list,
    otherwise it raises a ValueError
    
    - params
        - user_input [str]: The user's input
        - param valid_options [List[str]]: A list of strings that are valid options for the user to choose from

    - returns 
        - The user_input is being returned or raises a value error.
    """
    user_input = user_input.upper()
    options = list(map(lambda option: option.upper(), valid_options))
    if func.check_if_a_string_is_in_list(user_input, options):
        return user_input
    else:
        raise ValueError

def input_rail_data():
    """
    It asks the user for a curve, thread, date, reprofiling, and file location, and returns a dictionary
    with those values

    - returns 
        - A dictionary with the data that the user has inputted.
    """
    data = {}
    data["curve"] = func.user_input(int, "Insert the curve: ")
    data["thread"] = func.user_input(valid_input, "Insert rail thread: ", [["HA", "HB"]])
    data["date"] = func.user_input(datetime.fromisoformat, "Insert the date of the measurement [YYYY-MM-DD]: ")
    data["reprofiling"] = func.user_input(valid_input, "Insert yes or no if the measurement is from a reprofiled rail: ", [["yes", "no"]])
    data["raw_file"] = choose_a_file("Select the raw data file")
    data["filter_file"] = choose_a_file("Select the filter file")
    data["exc_file"] = choose_a_file("Select the exc_file")
    data["iso_file"] = choose_a_file("Select the iso file")
    return data

def insert_rail_data():
    data = input_rail_data()
    func.convert_value_to_string(data, "date")
    write_a_dictionary_in_a_json_file(data)

def main():
    insert_rail_data()

if __name__ == '__main__':
    main()