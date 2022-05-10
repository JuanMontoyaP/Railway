from functions.functions import key_value_json
from .read import read_json_file

from typing import List

def filter_json_data(value, data, key):
    """
    It takes a value, a list of dictionaries, and a key, and returns a list of dictionaries where the
    value of the key matches the value passed in
    
    Params 
        - value: The value you want to filter by
        - data: The JSON data
        - key: the key to filter on

    Returns: 
        - A list of dictionaries
    """
    return list(filter(lambda record: key_value_json(record, key) == value, data))

def data_available(keys: List[str]):
    """
    The function `data_available` takes a list of keys and returns a list of lists of values for each
    record in the JSON file
    
    - Params 
        - keys: List[str]
    
    - Return: 
        - A list of lists.
    """
    records = read_json_file("C:/Users/jpmon/Documents/Railway/data/rail_data.json")
    return [[record[key] for key in keys] for record in records]

def main():
    data = read_json_file("data/rail_data.json")
    print(filter_json_data("HA", data, "thread"))

if __name__ == '__main__':
    main()