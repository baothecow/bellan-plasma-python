## File contains specific plotting routines.

from file_io_lib import readVME
import matplotlib.pyplot as plt
from vme_plot import *
import idl_support as idlsup



def vme_plot_current(
        shots,
        title='Current vs time',
        ytitle='Current (kA)',
        xtitle='Time (' + '$\mu$' + 's)',
        xlim=[10,30],
        ylim=[-40, 40],
        smooth_win=50):
    """ Plots the current vs time of the shots """

    rows = 3                    # IV data has 3 rows.
    
    root = idlsup.get_idl_vme_path()

    for counter in range(0, len(shots)):
        constructor = '\\vi_t2ch13_' + str(shots[counter]) + '.dat'
        filename = root + idlsup.get_shot_date(shots[counter]) + constructor
        data = readVME(filename, rows=rows)
        time = data[0, :]
        signal = data[2, :]
        
        vme_plot_diagnostic(time, signal, diag='current')

#        vme_basic_2d_plot(
#            time,
#            signal, 
#            color_counter=counter,
#            title=title,
#            xtitle=xtitle,
#            ytitle=ytitle,
#            xlim=xlim,
#            ylim=ylim,
#            smooth_win=smooth_win)


    # Label the shot numbers.
    plt.figtext(.5,.85,'Shot(s): ' + ", ".join(shots), fontsize=10, ha='center')
    plt.show()    



  
    