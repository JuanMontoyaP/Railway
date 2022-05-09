from functions.functions import key_value_json
from .read import read_json_file

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

def main():
    data = read_json_file("data/rail_data.json")
    print(filter_json_data("HA", data, "thread"))

if __name__ == '__main__':
    main()