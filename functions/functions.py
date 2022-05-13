import sys
import re

from typing import List, Dict

def print_line(length: int = 70):
    """
    It prints a line of length 70
    
    - params
        - length: int = 70, defaults to 70
    """
    print(length*"=")

def print_message(msg: str, end: str ='\n'):
    """
    `print_message` takes a string and an optional string and prints the first string with the second
    string appended to the end
    
    - params 
        - msg [str]: The message to print
        - end [str] (optional): Specify what to print at the end. Default is \n, i.e. the new line character
    """
    print(msg, end=end)

def user_input(function, msg: str, kwargs=[]):
    """
    It takes a function, a message, and a list of arguments, and returns the value of the function
    applied to the input of the user
    
    - params
        - function: the function that will be used to convert the input to the desired type
        - msg [str]: The message to be displayed to the user
        - kwargs: a list of arguments to pass to the function
        
    returns 
        - The value of the input.
    """
    while True:
        value = input(msg)
        try :
            value = function(value, *kwargs)
            break
        except ValueError:
            print("Insert a valid value")
            pass
    return value

def check_if_a_string_is_in_list(my_string : str,values: List[str]) -> bool:
    """
    It checks if a string is valid by checking if it is equal to any of the values in a list of strings
    
    - params
        - my_string [str]: the string you want to check
        - values list[str]: the list of values you want to check
    - return: 
        - True if the string is in the list of values
    """
    return my_string in values

def convert_value_to_string(dictionary : Dict, key: str):
    """
    It takes a dictionary and a key, and converts the value of the key to a string
    
    - Params 
        - dictionary [Dict]: The dictionary you want to convert the value to a string
        - key [str]: The key of the dictionary whose value you want to convert to a string
    """
    dictionary[key] = str(dictionary[key])

def key_value_json(json_file, key):
    """Returns the key value of a json file."""
    try:
        return json_file[key]
    except KeyError as error:
        print(f'The key: {error} does not exist.')
        sys.exit()

def unique_items_in_nested_list(my_list: List[List]) -> List[List]:
    """
    It takes a list of lists, and returns a list of lists with all duplicates removed
    
    - Params 
        - my_list List[List]: Nested list 

    - Returns 
        - A list of lists of the unique items
    """
    unique_list = []
    [unique_list.append(item) for item in my_list if item not in unique_list]
    return unique_list

def split_strings_and_return_certain_values(my_string: str, delimiters: str, values: List[int] = []) -> List[str]:
    """
    It takes a string, splits it into a list of strings based on the delimiters provided, and returns
    the values in the list that are specified by the values parameter
    
    - Params: 
        - my_string [str]: The string you want to split
        - delimiters [str]: The delimiters you want to split the string by
        - values: List[int] = []

    - Return: 
        - List[str]: A list of strings
    """
    if values:
        return [re.split(delimiters, my_string)[ind] for ind in values]
    else:
        return re.split(delimiters, my_string)

def convert_a_string_into_dict(my_string: str, values: List[int], keys: List[str]):
    """
    It takes a string, splits it into a list, and then returns a dictionary with the values from the
    list as the values and the keys as the keys
    
    - Params 
        - my_string [str]: The string you want to convert into a dictionary
        - values List[int]: The indexes of the values of the strings you want to keep
        - keys List[str]: The keys of the dictionary

    - Returns 
        - A dictionary
    """
    string_list = split_strings_and_return_certain_values(my_string, ', | ', values)
    return dict(zip(keys, string_list))

def main():
    pass

if __name__ == '__main__':
    main()