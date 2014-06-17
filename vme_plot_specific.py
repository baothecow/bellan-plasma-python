## File contains specific plotting routines.


import matplotlib.pyplot as plt
import numpy as np
from vme_plot import *
from pylab import subplots_adjust
from vme_analyze import vme_avg_sig, vme_get_time_from_data, \
    vme_get_signal_from_data, get_b_from_bdot, get_b_from_hall, \
    vme_get_sig_min_and_max, vme_get_extra_from_data, vme_unflatten_list



## User defined parameters.
from parameters import plot_diag_params, diag_params



def vme_plot_diag_for_shots(shots_array, diag, descript="", delay=None, extra='', band=1):
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
                
        extra - specify which piece of extra information to return within a call.
                
        band - Checks to see if a band is also plotted.
    
    """
    
    # Start a new figure
    plt.figure()

    # Iterate through the shot numbers.
    for i in range(0, len(shots_array)):
        print shots_array[i]
        data = vme_avg_sig(shots_array[i], diag, extra=extra)
        time = vme_get_time_from_data(data, diag)
        # Allows time shifts to match plots
        if delay != None:
            print delay[i]
            time = np.add(time, delay[i])
        signal = vme_get_signal_from_data(data, diag)
        plot_diag_params['gen.shotnum'] = shots_array[i]
        
        extra_signals = ''  # Null value of extra_signal.
        if extra != '':
            extra_signals = vme_get_sig_min_and_max(vme_get_extra_from_data(data, diag), band)
            
        vme_plot_diagnostic(time, signal, diag, 
                            color=plot_diag_params['gen.color'+str(i)], extra_signals=extra_signals)

        
        
    # Generate legend for the figure using plt.figlegend
    handles, labels = plt.gca().get_legend_handles_labels()
    if plot_diag_params['gen.shotnum_legend']:
        plt.figlegend(handles, labels, loc=1, prop={'size':10})
    ## If an additional description is included, use it!
    if descript != "":
        plt.legend(handles, descript, loc=4)#, prop={'size':10})    
    plt.show()    
    
    
def plot_hall_for_shots(shots_array, descript="", delay=None, sensor='A', extra='', band=1):
    """ Plots the hall sensor vs time over multiple shots

        Input:        
        shots = A array with strings of shot num or lists of strings of shotnums
            
            Examples: 
            [['847']] : plot diagnostic for shot 847. (single line)
            [['847'], ['848'], ['849']] : plot diagnostic for shots 847, 848 and 849.
            [['847', '848'], '849'] : plot the average and 847 and 848 also plot 849.
                                
        descript - an array of strings containing additional description of
                each elment in shots_array.
                
        delay - an array of numbers containing the appropriate time delay in
                microseconds to be added to the VME time.
                
        sensor - The name of the sensor.  It must have a corresponding calibration
                matrix defined in vme_analyze.
                
    
    """
    
    diag = 'hall'
    diag_params['hall.sensor'] = sensor
    
    # Start a new figure
    plt.figure()

    # Iterate through the shot numbers.
    for i in range(0, len(shots_array)):
        print shots_array[i]
        plot_diag_params['gen.shotnum'] = shots_array[i]
        
        ## Unflatten the shot array by 1 level:  ['123', '124'] -> [['123], ['124']]
        unflatten_shot_arr = vme_unflatten_list(shots_array[i])
        
        indiv_signal_list = list()
        shots_bx = dict()
        shots_by = dict()
        shots_bz = dict()
        
        ## Extract data separately for each shot so that I can apply the transformation matrix individually.
        ## The nice thing is that I've essentially created the output that I would've gotten by
        ## Calling vme_get_extra_from_data.
        for j in range(0, len(unflatten_shot_arr)):
            indiv_data = vme_avg_sig(unflatten_shot_arr[j], diag, extra=extra)
            time = vme_get_time_from_data(indiv_data, diag)
            indiv_hall_signal = vme_get_signal_from_data(indiv_data, diag)
            indiv_b_signal = get_b_from_hall(indiv_hall_signal, sensor=sensor)
            indiv_signal_list.append(indiv_b_signal)
            
            ## Reformat the bx, by, bz information by shots to be compatible with
            ## vme_get_sig_min_and_max which expects a list of dicts.
            shots_bx[shots_array[i][j]] = np.multiply(indiv_b_signal[0])#, 1e4)
            shots_by[shots_array[i][j]] = np.multiply(indiv_b_signal[1])#, 1e4)
            shots_bz[shots_array[i][j]] = np.multiply(indiv_b_signal[2])#, 1e4)
            

        signal = np.mean(indiv_signal_list, axis=0)
    
        # Label of each input.
        plot_diag_params['gen.shotnum'] = shots_array[i]
        
        extra_signals = ''  # Null value of extra_signal.
        if extra != '':
            # Must create the list of dicts.
            signals_list = list()
            signals_list.append(shots_bx)
            signals_list.append(shots_by)
            signals_list.append(shots_bz)
            extra_signals = vme_get_sig_min_and_max(signals_list, band)
        
        vme_plot_diagnostic(time, np.multiply(signal, 1), diag+'.b',    \
                            color=plot_diag_params['gen.color'+str(i)], extra_signals=extra_signals)       
    
    # Generate legend for the figure using plt.figlegend
    handles, labels = plt.gca().get_legend_handles_labels()
    if plot_diag_params['gen.shotnum_legend']:
        plt.figlegend(handles, labels, loc=1, prop={'size':10})
    ## If an additional description is included, use it!
    if descript != "":
        plt.legend(handles, descript, loc=4)#, prop={'size':10})    
    plt.show()  
        
    plt.show()
    
    
def plot_sol_mpa_for_shots(shots_array, descript="", delay=0, num_probe=4):
    """ Used to plot the solar magnetic probe array 
    
    num_probe - determines how many probes to plot.
    
    """
    
    diag = 'sol_mpa'

    # Start a new figure
    fig, axes = plt.subplots(nrows=4, ncols=3)
    fig.tight_layout()

    # Iterate through the shot numbers.
    for i in range(0, len(shots_array)):
        print shots_array[i]
        for probenum in range(1, num_probe+1):
            
            ## Set plotting parameters.
            diag_params[diag+'.bx.ind'] = probenum
            diag_params[diag+'.by.ind'] = probenum
            diag_params[diag+'.bz.ind'] = probenum
            
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
            subplot = ((3, num_probe, (probenum)), (3, num_probe, (probenum)+num_probe), \
                (3, num_probe, (probenum)+(2*num_probe)))
            vme_cust_plot_diagnostic(time, signal, 'sol_mpa.int', subplot,
                                     color=plot_diag_params['gen.color'+str(i)])
                                     
    # Generate legend for the figure using plt.figlegend
    handles, labels = plt.gca().get_legend_handles_labels()
    if plot_diag_params['gen.shotnum_legend']:
        plt.figlegend(handles, labels, loc=1, prop={'size':10})
    ## If an additional description is included, use it!
    if descript != "":
        plt.legend(handles, descript, loc=4)#, prop={'size':10})    
    plt.show()  
        
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

  
    