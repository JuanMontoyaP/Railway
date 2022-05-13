import functions.functions as fun
from .read import read_json_file

from typing import List, Dict
from datetime import datetime

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
    return list(filter(lambda record: fun.key_value_json(record, key) == value, data))

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
    records = read_json_file("C:/Users/jpmon/Documents/Railway/data/db/rail_data.json")
    return [[record[key] for key in keys] for record in records]

def filter_curves(curve_str: str, indexes: List[int], keys: List[str]) -> List[Dict]:
    """
    It takes a string, converts it into a dictionary, and then filters a list of dictionaries based on
    the dictionary
    
    - Params 
        - curve_str [str]: 'curve xx, HA, date 2020-01-01'
        - indexes List[int]: Indexes of the important data in curve_str
        - keys List[str]: Keys for 'curve', 'thread' and so on
    
    - Returns 
        - A list of dictionaries of the selected curve.
    """
    filter_dic = fun.convert_a_string_into_dict(curve_str, indexes, keys)
    for key in filter_dic.keys():
        if key == 'curve':
            filter_dic[key] = int(filter_dic[key])  # type: ignore
        elif key == 'date':
            filter_dic[key] = str(datetime.strptime(filter_dic[key], '%Y-%m-%d'))

    records = read_json_file("C:/Users/jpmon/Documents/Railway/data/db/rail_data.json")
    return filter_data(filter_dic, records)

def main():
    data = read_json_file("data/rail_data.json")
    print(filter_json_data("HA", data, "thread"))

if __name__ == '__main__':
    main()