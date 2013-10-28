""" Plot VME currents and voltage data of array of shot numbers

    Attempt at adding a docstring.

"""

## VME plotting routines
import matplotlib.pyplot as plt



## Plots VME data.
def vme_plot_current(
        data, title="", xtitle="", ytitle=""):

    
    plt.plot([1, 2, 3, 4])
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.show()


