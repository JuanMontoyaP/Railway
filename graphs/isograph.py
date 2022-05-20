from datahandling.read import read_catdata

import matplotlib.pyplot as plt
import numpy as np

from typing import Dict

wavelengths_iso = np.array([630, 500, 400, 315, 250, 200, 160, 125, 100, 80.0, 63.0, 50.0, 40.0, 31.5, 25.0, 20.0, 16.0, 12.5, 10.0, 8.0, 6.3])
frequency_iso = np.array([23.5, 21.7, 19.8, 18.0, 16.1, 14.3, 12.4, 10.6, 8.8, 6.9, 5.1, 3.2, 1.4, -0.5, -2.3, -4.1, -6.0, -7.8, -9.7, -9.7, -9.7])

def roughness_level_plot(x, y1, names, title, y2=[]):
    
    if (names[0] == 'Before'):
        line = '-s'
    else:
        line = 'g-o'

    names.append('ISO 3095')

    fig, ax = plt.subplots()
    ax.semilogx(x, y1, line)
    if len(y2): ax.semilogx(x, y2, 'g-o')
    ax.semilogx(wavelengths_iso, frequency_iso, '--')

    ax.invert_xaxis()
    ax.set_title(title)
    ax.set_xlabel('Wavelength $[mm]$')
    ax.set_ylabel('Roughness level $[dB]$')

    ax.legend(names)

    plt.tight_layout()
    return fig

def iso_data_graph(record: Dict):
    data = read_catdata(record["iso_file"], death_lines=6)
    roughness_level_plot(data[:,0], data[:,1], ['Before'], 'ISO Data Curve: %d' % record["curve"])
    fig_name = "data/figures/iso_curve{}_{}_{}.png".format(record['curve'], record["thread"], record["date"][:10])
    plt.savefig(fig_name, format="png")

def main():
    pass

if __name__ == '__main__':
    main()