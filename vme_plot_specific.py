## File contains specific plotting routines.

from file_io_lib import readVME
import matplotlib.pyplot as plt
from vme_plot import *
import idl_support as idlsup
from pylab import subplots_adjust
from vme_analyze import get_diag_constructor, vme_avg_sig



def vme_plot_current(shots):
    """ Plots the current vs time of the shots """

    rows = 3                    # IV data has 3 rows.
    
    root = idlsup.get_idl_vme_path()

    for counter in range(0, len(shots)):
        constructor = '\\vi_t2ch13_' + str(shots[counter]) + '.dat'
        filename = root + idlsup.get_shot_date(shots[counter]) + constructor
        data = readVME(filename, rows=rows)
        time = data[0, :]
        signal = data[2, :]
        plot_diag_params['gen.shotnum'] = shots[counter]
        vme_plot_diagnostic(time, signal, diag='current', 
                            color=plot_diag_params['gen.color'+str(counter)])
    # Generate legend
    plt.legend()
    # Label the shot numbers.
    plt.figtext(.5,.85,'Shot(s): ' + ", ".join(shots), fontsize=10, ha='center')
    plt.show()    
    
def vme_plot_diag_for_shots(shots_array, diag='current', descript=""):
    """ Plots the diagnostic vs time over multiple shots

        Input:        
        shots = A array with strings of shot num or lists of strings of shotnums
            
            Examples: 
            ['847'] : plot diagnostic for shot 847. (single line)
            ['847', '848', '849'] : plot diagnostic for shots 847, 848 and 849.
            [['847', '848'], '849'] : plot the average and 847 and 848 also plot 849.
            
                
        diag:   string denoting the wanted diagnostics.
                    * 'current' is rogowski coil current.
                    * 'tek_hv' is Tektronic high voltage'
                    * 'iso_hv' is Xiang's Isolated high voltage probe
                    
        descript - an array of strings containing additional description of
                each elment in shots_array.
    
    """

    # Iterate through the shot numbers.
    for i in range(0, len(shots_array)):
        print shots_array[i]
        data = vme_avg_sig(shots_array[i], diag=diag)
        time = data[0]
        signal = data[1]
        plt.plot(time,signal)
        plt.show()
        plot_diag_params['gen.shotnum'] = shots_array[i]
        vme_plot_diagnostic(time, signal, diag=diag, 
                            color=plot_diag_params['gen.color'+str(i)])
    # Generate legend
    legend1 = plt.legend(prop={'size':10})
    if descript != "":
        handles, labels = plt.gca().get_legend_handles_labels()
        plt.legend(handles, descript, loc=4, prop={'size':10})
        # Creation of new removes legend1 so add legend1 as separate artist.
        plt.gca().add_artist(legend1)
        
    plt.show()    

## Plot of two signals with common time axis.
def vme_2diag_2d_plot(
        time,
        signal_1,
        signal_2,
        diag1='tek_hv',
        diag2='current',
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls']
        ):
    """ 2D Plot of two signals with common time axis. """

    # Set title of the first plot is now the title of the whole plot.
    newtitle = plot_diag_params[diag1 + '.name'] + ' & ' + \
        plot_diag_params[diag2 + '.name'] + ' vs Time'
    plot_diag_params[diag1 + '.title'] = newtitle

    ## Generate the two subplot by calling the basic plot function for
    ## each subplot.    
    
    plt.subplot(211)
    vme_plot_diagnostic(time, signal_1, diag=diag1, color=color, ls=ls)
    
    plt.subplot(212)
    plot_diag_params[diag2 + '.title'] = ""    ## Removes the second title.
    vme_plot_diagnostic(time, signal_2, diag=diag2, color=color, ls=ls)

    ## Remove the spacing between the subplots
    subplots_adjust(hspace=0.001)

  
    