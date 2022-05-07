import userinterface.ui as ui
from datahandling.insert_data import insert_rail_data
def main():
    # selection = ui.main_page()
    # rail_roughness = read_data()
    insert_rail_data()
    # TODO Calculate the growth factor
    # TODO Calculate when the rail is going to fail
    # TODO Tell the user when the rail is going to fail
    # TODO Show the graphs with the three norms 
    pass

if __name__ == "__main__":
    main()