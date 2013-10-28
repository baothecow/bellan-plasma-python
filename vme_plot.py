""" Plot VME currents and voltage data of array of shot numbers

    Attempt at adding a docstring.

"""

## VME plotting routines
import matplotlib.pyplot as plt



## Plots VME data.
def vme_plot_current(
        data,
        title = 'Plot of VME current',
        xtitle = 'Time (' + '$\mu$' + 's)',
        ytitle = "Current (kA)",
        xlim = [10, 30],
        ylim = [-40, 40]):

    time = data[0, :]
    current = data[2, :]

    plt.plot(time, current, 'r-')
    plt.plot(time, 
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()


