import sys
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

def main():
    pass

if __name__ == '__main__':
    main()