import sys

import pages.mainpage as mp
import pages.insertpage as ip
import pages.reportspage as rp

from reports import reports as rep

# A function that is being called from the mainpage.py file.
def main():
    selection = mp.main_page()
    if selection == 1:
        ip.insert_page()
    elif selection == 2:
        rp.reports_page()
    else:
        sys.exit("Exit program")
    
    # rep.generate_reports("Curve 13, HA, date 2021-12-16")
    # rail_roughness = read_data()

    # TODO Calculate the growth factor
    # TODO Calculate when the rail is going to fail
    # TODO Tell the user when the rail is going to fail
    # TODO Show the graphs with the three norms 
    pass

if __name__ == "__main__":
    main()