from typing import List
from tkinter import Tk 
from tkinter.filedialog import askopenfilename

def choose_a_file() -> str:
    """
    It opens a file dialog box and returns the path to the file selected
    :return: The file path of the file that was selected.
    """
    Tk().withdraw()
    filename = askopenfilename(title='Choose a file')
    return filename

def choose_files(number_of_files) -> List[str]:
    """
    It returns a list of strings, each of which is the name of a file chosen by the user
    
    :param number_of_files: The number of files you want to choose
    :return: A list of strings.
    """
    return [choose_a_file() for _ in range(number_of_files)]

def main():
    files = choose_files(2)
    print(files)

if __name__ == '__main__':
    main()