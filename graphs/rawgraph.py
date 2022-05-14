from datahandling.read import read_catdata
from .graph import graph_data

import matplotlib.pyplot as plt

from typing import Dict

def raw_data_graph(record: Dict):
    """
    `raw_data_graph`

    It reads the raw data file, plots the data, and saves the figure
    
    - Args:
      - record (Dict): Dict
    """
    data = read_catdata(record["raw_file"])
    graph_data(data, ["Raw Data Curve: %d" % record["curve"] , "Position $[km]$", "Raw Disp $[\mu m]$"]) #type: ignore
    fig_name = "data/figures/raw_curve{}_{}_{}.png".format(record['curve'], record["thread"], record["date"][:10])
    plt.savefig(fig_name, format="png")

def main():
    pass

if __name__ == '__main__':
    main()