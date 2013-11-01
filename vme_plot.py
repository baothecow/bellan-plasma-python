""" Plot VME currents and voltage data of array of shot numbers

    Attempt at adding a docstring.

"""

## VME plotting routines
import matplotlib.pyplot as plt
from cookb_signalsmooth import smooth

## User defined parameters.
from parameters import plot_diag_params


## Basic 2D plot of signal vs time.
def vme_basic_2d_plot(
        time,
        signal, 
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls'],
        title=plot_diag_params['gen.title'],
        xtitle=plot_diag_params['gen.xtitle'],
        ytitle=plot_diag_params['gen.ytitle'],
        xlim=plot_diag_params['gen.xlim'],
        ylim=plot_diag_params['gen.ylim'],
        ):
    """ Basic 2D plotting of a single quantity vs time """

    ## Plot the raw version using a thin line. 
    raw = plt.plot(time, signal)
    plt.setp(raw, color=color, ls=ls)
    plt.setp(raw, label=plot_diag_params['gen.shotnum'])
    
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    return raw


## Basic 2D plot of signal vs time.
def vme_smooth_2d_plot(
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
    
    ## Plot the raw version using a thin line. 
    raw = plt.plot(time, signal)
    plt.setp(raw, color=color, ls=ls)
    plt.setp(raw, linewidth=plot_diag_params['gen.thin_ln_width'])
    
    ## Plot the smoothed version using a thicker line.
    smoothed = plt.plot(time, smooth(signal, window_len=smooth_win))
    plt.setp(smoothed, color=color, ls=ls)
    plt.setp(smoothed, linewidth=plot_diag_params['gen.thick_ln_width'])
    plt.setp(smoothed, label=plot_diag_params['gen.shotnum'])

 
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    return smoothed
  

def vme_plot_diagnostic(
        time, 
        signal,
        diag='current',
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls']
        ):
    """ Plots diagnostics of an array of shotnumbers """
    
    return vme_smooth_2d_plot(
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
    