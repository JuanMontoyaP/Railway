from functions.functions import key_value_json
from .read import read_json_file

from typing import List, Dict

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

def filter_data(filter_dict: Dict, data: List[Dict]) -> List[Dict]:
    """
    It takes a dictionary of filters and a list of dictionaries and returns a list of dictionaries that
    match the filters
    
    - Params 
        - filter_dict [Dict]: This is the dictionary that contains the filter criteria
        - data List[Dict]: Data to be filtered

    - Returns: 
        - A list of dictionaries.
    """
    records = data
    for key,value in filter_dict.items():
        records = filter_json_data(value, records, key)
    return records

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