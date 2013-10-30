""" Plot VME currents and voltage data of array of shot numbers

    Attempt at adding a docstring.

"""

## VME plotting routines
import matplotlib.pyplot as plt
from cookb_signalsmooth import smooth
from pylab import subplots_adjust


## Basic 2D plot of signal vs time.
def vme_basic_2d_plot(
        time,
        signal, 
        style_counter = 0,                # used to determine specific colors.
        title = '2D Signal vs Time',
        xtitle = 'Time (' + '$\mu$' + 's)',
        ytitle = 'Signal',
        xlim = [10, 30],
        ylim = [-40, 40],
        smoothing_window = 50):
    """ Basic 2D plotting of a single quantity vs time """

    plot_style = color_array[style_counter] + style_array[style_counter]

    ## Plot the raw version using a thin line. 
    plt.plot(time, signal, plot_style, linewidth=0.5)
    ## Plot the smoothed version using a thicker line.
    plt.plot(time, smooth(signal, window_len=smoothing_window), plot_style,
             linewidth=2)
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)


## Plot of two signals with common time axis.
def vme_2params_2d_plot(
        time,
        signal_1,
        signal_2,
        style_counter = 0,                # used to determine specific colors.
        title = '2D Plot vs Time',
        xtitle1 = 'Time (' + '$\mu$' + 's)',
        ytitle1 = '',
        xlim1 = [10, 30],
        ylim1 = [-40, 40],
        smoothing_window_1 = 50,
        xtitle2 = 'Time (' + '$\mu$' + 's)',
        ytitle2 = '',
        xlim2 = [10, 30],
        ylim2 = [-40, 40],
        smoothing_window_2 = 50):
    """ 2D Plot of two signals with common time axis. """

    plot_style = color_array[style_counter] + style_array[style_counter]

    ## Generate the two subplot by calling the basic plot function for
    ## each subplot.
    plt.subplot(211)
    vme_basic_2d_plot(
        time,
        signal_1,
        style_counter=style_counter,
        xtitle=xtitle1,
        ytitle=ytitle1,
        xlim=xlim1,
        ylim=ylim1,
        smoothing_window=smoothing_window_1)
    plt.subplot(212)
    vme_basic_2d_plot(
        time,
        signal_2,
        title='',           # Clears out title of lower plot.
        style_counter=style_counter,
        xtitle=xtitle2,
        ytitle=ytitle2,
        xlim=xlim2,
        ylim=ylim2,
        smoothing_window=smoothing_window_2)

    ## Remove the spacing between the subplots
    subplots_adjust(hspace=0.001)
        

### Some colors and styles.

color_array = ['r', 'b', 'g', 'c', 'm', 'y', 'k']
style_array = ['-', '-', '-', '-', '-', '-', '-']
