from datahandling.insert_data import insert_rail_data
from functions.functions import convert_value_to_string

import json

from typing import Dict

def write_a_dictionary_in_a_json_file(data_dictionary: Dict, file_name : str = "data/rail_data.json"):
    """
    It opens a file, reads the data in the file, appends the data_dictionary to the data, and then
    writes the data back to the file
    
    - Params 
        - data_dictionary: The dictionary that you want to write in the json file
        - file_name [str] (Optional): The name of the file you want to write to, defaults to data/rail_data.json
    """
    with open(file_name, "r+", encoding="utf-8") as f:
        data = json.load(f)
        data.append(data_dictionary)
        f.seek(0)
        json.dump(data, f)

def main():
    data = insert_rail_data()
    convert_value_to_string(data, "date")
    write_a_dictionary_in_a_json_file(data)

if __name__ == '__main__':
    main()