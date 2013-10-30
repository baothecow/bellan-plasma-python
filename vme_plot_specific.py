## File contains specific plotting routines.

from file_io_lib import readVME
import matplotlib.pyplot as plt
from vme_plot import vme_basic_2d_plot



def vme_plot_current(
        shots,
        title='Current vs time',
        ytitle='Current (kA)',
        xtitle='Time (' + '$\mu$' + 's)',
        color_counter=0,
        style_counter=0,
        xlim=[10,30],
        ylim=[-40, 40],
        smoothing_window=50):
    """ Plots the current vs time of the shots """

    rows = 3
    root = 'G:\\data\\singleloop\\singleloop_VME\\data\\'
    foldername = '2013.03.14\\'

    for counter in range(0, len(shots)):
        constructor = 'vi_t2ch13_' + str(shots[counter]) + '.dat'
        filename = root + foldername + constructor
        data = readVME(filename, rows=rows)
        time = data[0, :]
        signal = data[2, :]

        vme_basic_2d_plot(
            time,
            signal, 
            color_counter=counter,
            title=title,
            xtitle=xtitle,
            ytitle=ytitle,
            xlim=xlim,
            ylim=ylim,
            smoothing_window=smoothing_window)


    # Label the shot numbers.
    plt.figtext(.5,.85,'Shot(s): ' + ", ".join(shots), fontsize=10,ha='center')
    plt.show()    
