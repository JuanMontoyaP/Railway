from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

import numpy.typing as npt
from typing import List

def graph_data(data: npt.NDArray[np.float64], labels: List[str] = ["Title", "X", "Y"], figsize: tuple = (12,6)) -> Figure:
    """
    `graph_data`

    It takes a 2D array of data, and plots it with the first column as the x-axis, and the second column
    as the y-axis.
    
    - Args:
      - data (npt.NDArray[np.float64]): The data to plot.
      - labels (List[str]): a list of strings that will be used as the title, x-axis label, and y-axis label.
      - figsize (tuple): tuple = (12,6)
    
    - Returns:
      - A figure object.
    """
    fig , ax = plt.subplots(figsize=figsize)
    ax.plot(data[:,0], data[:,1])
    ax.set_xlim([data[0,0], data[-1,0]])
    ax.set_title(labels[0])
    ax.set_xlabel(labels[1])
    ax.set_ylabel(labels[2])
    plt.tight_layout()
    return fig

def main():
    pass

if __name__ == "__main__":
    main()