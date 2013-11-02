""" Plot VME currents and voltage data of array of shot numbers

    Attempt at adding a docstring.

"""

## VME plotting routines
import matplotlib.pyplot as plt
from cookb_signalsmooth import smooth

## User defined parameters.
from parameters import plot_diag_params, diag_params


### Basic 2D plot of signal vs time.
#def vme_basic_2d_plot(
#        time,
#        signal, 
#        color=plot_diag_params['gen.color'],
#        ls=plot_diag_params['gen.ls'],
#        title=plot_diag_params['gen.title'],
#        xtitle=plot_diag_params['gen.xtitle'],
#        ytitle=plot_diag_params['gen.ytitle'],
#        xlim=plot_diag_params['gen.xlim'],
#        ylim=plot_diag_params['gen.ylim'],
#        ):
#    """ Basic 2D plotting of a single quantity vs time """
#
#    ## Plot the raw version using a thin line. 
#    raw = plt.plot(time, signal)
#    plt.setp(raw, color=color, ls=ls)
#    plt.setp(raw, label=plot_diag_params['gen.shotnum'])
#    
#    plt.title(title)
#    plt.ylabel(ytitle)
#    plt.xlabel(xtitle)
#    plt.xlim(xlim)
#    plt.ylim(ylim)
#    
#    return raw


## Basic 2D plot of signal vs time.
def vme_2d_plot_scalar(
        time,
        signal, 
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls'],
        title=plot_diag_params['gen.title'],
        xtitle=plot_diag_params['gen.xtitle'],
        ytitle=plot_diag_params['gen.ytitle'],
        xlim=plot_diag_params['gen.xlim'],
        ylim=plot_diag_params['gen.ylim'],
        smooth_win=plot_diag_params['gen.smooth_win']):
    """ Basic 2D plotting of a single quantity vs time """
    
        
    
    ## Check to see if raw is wanted.
    if plot_diag_params['gen.include.raw']:
        ## Plot the raw version using a thin line
        raw = plt.plot(time, signal)
        plt.setp(raw, color=color, ls=ls)
        plt.setp(raw, linewidth=plot_diag_params['gen.thin_ln_width'])
    
    ## Plot the smoothed version using a thicker line.
    smoothed_signal = smooth(signal, window_len=smooth_win)
    smoothed = plt.plot(time, smoothed_signal)
    plt.setp(smoothed, color=color, ls=ls)
    plt.setp(smoothed, linewidth=plot_diag_params['gen.thick_ln_width'])
    plt.setp(smoothed, label=plot_diag_params['gen.shotnum'])

 
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    return smoothed
    
## Plot of all three vector components.
def vme_2d_plot_vector(
        time,
        vector, 
        diag='sol_mpa',
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls'],
        title=plot_diag_params['gen.title'],
        xtitle=plot_diag_params['gen.xtitle'],
        ytitle=plot_diag_params['gen.ytitle'],
        xlim=plot_diag_params['gen.xlim'],
        ylim=plot_diag_params['gen.ylim'],
        smooth_win=plot_diag_params['gen.smooth_win']):
    """ Plot each vector components as individual plots aligned appropriately """


    
    ## Loop through the components of the vector
    for i in range(0, len(vector)):
        plt.subplot(plot_diag_params[diag+'.subplot.styles'][i])
        raw = plt.plot(time, vector[i])
        plt.setp(raw, color=color, ls=ls)
        plt.setp(raw, label=plot_diag_params['gen.shotnum'] + ': ' + \
                 plot_diag_params['gen.vector.label'][i])
        plt.title(plot_diag_params[diag+'.subplot.titles'][i])
        plt.xlabel(plot_diag_params[diag+'.subplot.xtitles'][i])
        plt.ylabel(plot_diag_params[diag+'.subplot.ytitles'][i])
        plt.xlim(xlim)
        plt.ylim(ylim)
 
     

  

def vme_plot_diagnostic(
        time, 
        signal,
        diag='current',
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls']
        ):
    """ Plots diagnostics of an array of shotnumbers """
    
    
    if diag_params[diag+'.datatype'] == 'scalar':
        return vme_2d_plot_scalar(
            time, 
            signal,
            color=color,
            ls=ls,
            title=plot_diag_params[diag + '.title'],
            xtitle=plot_diag_params[diag + '.xtitle'],
            ytitle=plot_diag_params[diag + '.ytitle'],
            xlim=plot_diag_params[diag + '.xlim'],
            ylim=plot_diag_params[diag + '.ylim']
            )
    
    if diag_params[diag+'.datatype'] == 'vector':
        return vme_2d_plot_vector(
            time, 
            signal,
            diag=diag,
            color=color,
            ls=ls,
            title=plot_diag_params[diag + '.title'],
            xtitle=plot_diag_params[diag + '.xtitle'],
            ytitle=plot_diag_params[diag + '.ytitle'],
            xlim=plot_diag_params[diag + '.xlim'],
            ylim=plot_diag_params[diag + '.ylim']
            )
    