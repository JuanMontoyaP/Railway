from datahandling.read import read_catdata
from .graph import graph_data

import matplotlib.pyplot as plt

from typing import Dict

def filter_data_graph(record: Dict):
    data = read_catdata(record["filter_file"])
    graph_data(data, ["Filter Data Curve: %d" % record["curve"] , "Position $[km]$", "30-100mm Disp $[\mu m]$"]) #type: ignore
    fig_name = "data/figures/filter_curve{}_{}_{}.png".format(record['curve'], record["thread"], record["date"][:10])
    plt.savefig(fig_name, format="png")

def main():
    pass

if __name__ == '__main__':
    main()