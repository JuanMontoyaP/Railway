from typing import List
import numpy.typing as npt

import json
import numpy as np
from tkinter import Tk 
from tkinter.filedialog import askopenfilename

def choose_a_file(msg: str = 'Choose a file') -> str:
    """
    It creates a Tkinter window, withdraws it, and then asks the user to choose a file
    - return:
        - The file path of the file that was chosen.
    """
    while True:
        Tk().withdraw()
        filename = askopenfilename(title=msg)
        if filename:
            break
        else:
            print("Select a file")
    return filename

def choose_files(number_of_files: int) -> List[str]:
    """
    It returns a list of file names, where each file name is chosen by calling the choose_a_file
    function
    
    - params: 
        - number_of_files [int]: The number of files you want to choose

    - return: 
        - A list of strings with the names of the files chosen.
    """
    return [choose_a_file() for _ in range(number_of_files)]

def read_isodata(file : str) -> npt.NDArray[np.float64]:
    """
    It reads the first six lines of the file, then reads the rest of the lines and converts them to
    floats
    
    - params
        - file [str]: The file to read from

    - return 
        - A numpy array of the data from the file.
    """
    data = []

    with open(file, "r") as f:
        for _ in range(6):
            f.readline()
        lines = f.readlines()

    for line in lines:
        data.append([float(x) for x in line.split()])

    return np.array(data)

def read_files(num_files: int, files: List[str]) -> npt.NDArray[np.float64]:
    """
    It reads in a list of files, and returns a 2D array with the first column being the wavelength, and
    the other columns being the data from each file
    
    - params
        - num_files [int]: number of files to read
        - files [list[str]]: List of files to read
        
    - return: 
        - A 2D array of 26 rows and num_files+1 columns.
    """
    data = np.zeros((26,num_files+1))
    for i, file in enumerate(files):
        data_file = read_isodata(file)
        data[:,i+1] = data_file[:,1]
        if not i:
            data[:,i] = data_file[:,0]
    return data

def read_data() -> npt.NDArray[np.float64]:
    """
    It reads the data from the files
    
    - return: 
        - A numpy array of float64
    """
    number_of_files = int(input("Introduce the number of files: "))
    files = choose_files(number_of_files)
    return read_files(number_of_files, files)

def read_json_file(filename: str):
    """
    It reads a JSON file and returns the data
    
    Params 
        - filename [str]: The route of the file to read

    Returns 
        - The data from the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def main():
    file_name = choose_a_file()
    print(read_json_file(file_name))

if __name__ == '__main__':
    main()