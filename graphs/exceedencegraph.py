from datahandling.read import read_catdata
from .graph import graph_data

import matplotlib.pyplot as plt

from typing import Dict

def exceedence_data_graph(record: Dict):
    data = read_catdata(record["exc_file"])
    graph_data(data, ["Exceedence Data Curve: %d" % record["curve"] , "Abs Disp $[\mu m]$", "Exceedence $[\%]$"], (6,6)) #type: ignore
    plt.axhline(y=5, color='grey', linestyle='--')
    plt.axvline(x=10, color='grey', linestyle='--')
    fig_name = "data/figures/exc_curve{}_{}_{}.png".format(record['curve'], record["thread"], record["date"][:10])
    plt.savefig(fig_name, format="png")

def main():
    pass

if __name__ == '__main__':
    main()