import sys

from pages import mainpage as mp
from pages import insertpage as ip

def main():
# A commented code that is not being used.
    selection = mp.main_page()
    if selection == 1:
        ip.insert_page()
    elif selection == 2:
        pass
    else:
        sys.exit("Exit program")
    
    # rail_roughness = read_data()

    # TODO Calculate the growth factor
    # TODO Calculate when the rail is going to fail
    # TODO Tell the user when the rail is going to fail
    # TODO Show the graphs with the three norms 
    pass

if __name__ == "__main__":
    main()