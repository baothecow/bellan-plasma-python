""" Plot VME currents and voltage data of array of shot numbers

    Attempt at adding a docstring.

"""

## VME plotting routines
import matplotlib.pyplot as plt
from cookb_signalsmooth import smooth



## Plots VME data.
def vme_plot_current(
        data,
        style_counter = 0,                # used to determine specific colors.
        title = 'Plot of VME current',
        xtitle = 'Time (' + '$\mu$' + 's)',
        ytitle = "Current (kA)",
        xlim = [10, 30],
        ylim = [-40, 40],
        smoothing_window = 50):

    time = data[0, :]
    current = data[2, :]

    plot_style = color_array[style_counter] + style_array[style_counter]

    ## Plot the raw version using a thin line. 
    plt.plot(time, current, plot_style, linewidth=0.5)
    ## Plot the smoothed version using a thicker line.
    plt.plot(time, smooth(current, window_len=smoothing_window), plot_style,
             linewidth=2)
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)


## Plots VME data.
def vme_basic_2d_plot(
        data,
        style_counter = 0,                # used to determine specific colors.
        title = '2D Plot vs Time',
        xtitle = 'Time (' + '$\mu$' + 's)',
        ytitle = '',
        xlim = [10, 30],
        ylim = [-40, 40],
        smoothing_window = 50):
    """ Basic 2D plotting of a single quantity vs time """

    time = data[0, :]
    current = data[2, :]

    plot_style = color_array[style_counter] + style_array[style_counter]

    ## Plot the raw version using a thin line. 
    plt.plot(time, current, plot_style, linewidth=0.5)
    ## Plot the smoothed version using a thicker line.
    plt.plot(time, smooth(current, window_len=smoothing_window), plot_style,
             linewidth=2)
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)


### Some colors and styles.

color_array = ['r', 'b', 'g', 'c', 'm', 'y', 'k']
style_array = ['-', '-', '-', '-', '-', '-', '-']
