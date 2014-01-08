## File contains specific plotting routines.


import matplotlib.pyplot as plt
import numpy as np
from vme_plot import *
from pylab import subplots_adjust
from vme_analyze import vme_avg_sig, vme_get_time_from_data, \
    vme_get_signal_from_data, get_b_from_bdot



## User defined parameters.
from parameters import plot_diag_params, diag_params



def vme_plot_diag_for_shots(shots_array, diag, descript="", delay=None):
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
                
        delay - an array of numbers containing the appropriate time delay in
                microseconds to be added to the VME time.
    
    """
    
    # Start a new figure
    plt.figure()

    # Iterate through the shot numbers.
    for i in range(0, len(shots_array)):
        print shots_array[i]
        data = vme_avg_sig(shots_array[i], diag)
        time = vme_get_time_from_data(data, diag)
        # Allows time shifts to match plots
        if delay != None:
            print delay[i]
            time = np.add(time, delay[i])
        signal = vme_get_signal_from_data(data, diag)
        plot_diag_params['gen.shotnum'] = shots_array[i]
        vme_plot_diagnostic(time, signal, diag, 
                            color=plot_diag_params['gen.color'+str(i)])       
    # Generate legend for the figure using plt.figlegend
    handles, labels = plt.gca().get_legend_handles_labels()
    legend1 = plt.figlegend(handles, labels, loc=1, prop={'size':10})
    ## If an additional description is included, use it!
    if descript != "":
        plt.figlegend(handles, descript, loc=4)#, prop={'size':10})
        # Creation of new removes legend1 so add legend1 as separate artist.
        plt.gca().add_artist(legend1)
        
    plt.show()    
    

    
def plot_sol_mpa_for_shots(shots_array, descript="", delay=0):
    """ Used to plot the solar magnetic probe array across all for probes """
    
    diag = 'sol_mpa'

    # Start a new figure
    fig, axes = plt.subplots(nrows=4, ncols=3)
    fig.tight_layout()

    # Iterate through the shot numbers.
    for i in range(0, len(shots_array)):
        print shots_array[i]
        for probenum in range(1, 5):
            
            ## Set plotting parameters.
            diag_params['gen.probenum'] = probenum
            plot_diag_params[diag+'.int.subplot.titles'] = ['Probe ' + str(probenum), \
                '', '']
                
            # Clean up the plot.
            if probenum == 1:
                plot_diag_params[diag+'.int.subplot.ytitles'] = ['Bx (G)', 'By (G)', 'Bz (G)']
            else:
                plot_diag_params[diag+'.int.subplot.ytitles'] = ['', '', '']
                
            ## Get data from saved files.
            data = vme_avg_sig(shots_array[i], diag)
            time = vme_get_time_from_data(data, diag)
            signal = get_b_from_bdot(time, vme_get_signal_from_data(data, diag))
            
            if delay != 0:
                print delay[i]
                time = np.add(time, delay[i])            
            
            plot_diag_params['gen.shotnum'] = shots_array[i]
            subplot = ((3, 4, (probenum)), (3, 4, (probenum)+4), (3, 4, (probenum)+8))
            vme_cust_plot_diagnostic(time, signal, 'sol_mpa.int', subplot,
                                     color=plot_diag_params['gen.color'+str(i)])
                                     
    # Generate legend for the figure using plt.figlegend
    handles, labels = plt.gca().get_legend_handles_labels()
    legend1 = plt.figlegend(handles, labels, loc=1, prop={'size':10})
    ## If an additional description is included, use it!
    if descript != "":
        plt.figlegend(handles, descript, loc=4, prop={'size':10})
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

  
    