""" Plot VME currents and voltage data of array of shot numbers

    Attempt at adding a docstring.

"""

## VME plotting routines
import matplotlib.pyplot as plt
from cookb_signalsmooth import smooth

## User defined parameters.
from parameters import plot_diag_params, diag_params



## Basic 2D plot of signal vs time.
def vme_2d_plot_scalar_signal(
        time,
        signal, 
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls'],
        subplot=plot_diag_params['gen.subplot.scalar'],
        title=plot_diag_params['gen.title'],
        xtitle=plot_diag_params['gen.xtitle'],
        ytitle=plot_diag_params['gen.ytitle'],
        xlim=plot_diag_params['gen.xlim'],
        ylim=plot_diag_params['gen.ylim'],
        smooth_win=plot_diag_params['gen.smooth_win'],
        label=True):
    """ Basic 2D plotting of a single quantity vs time """    
    
    ## Check to see if raw is wanted.
    if plot_diag_params['gen.include.raw']:
        ## Plot the raw version using a thin line
        raw = plt.plot(time, signal)
        plt.setp(raw, color=color, ls=ls)
        plt.setp(raw, linewidth=plot_diag_params['gen.thin_ln_width'])
    
    ## Plot the smoothed version using a thicker line.
    smoothed = plt.plot(time, smooth(signal, window_len=smooth_win))
    plt.setp(smoothed, color=color, ls=ls)
    plt.setp(smoothed, linewidth=plot_diag_params['gen.thick_ln_width'])
    
    # Label the plot.
    if label: plt.setp(smoothed, label=plot_diag_params['gen.shotnum'])

 
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)
    
    return smoothed
    
## Plot of all three vector components.
def vme_2d_plot_vector_signal(
        time,
        signals, 
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls'],
        subplot=plot_diag_params['gen.subplot.vector'],
        title=plot_diag_params['gen.title'],
        subplot_title=plot_diag_params['gen.subplot.titles'],
        subplot_xtitle=plot_diag_params['gen.subplot.xtitles'],
        subplot_ytitle=plot_diag_params['gen.subplot.ytitles'],
        xlim=plot_diag_params['gen.xlim'],
        ylim=plot_diag_params['gen.ylim'],
        smooth_win=plot_diag_params['gen.smooth_win'],
        label=True):
    """ Plot each vector components as individual plots aligned appropriately """

   
    ## Loop through the components of the vector
    for i in range(0, len(signals)):
        plt.subplot(subplot[i])
        
        smooth = vme_2d_plot_scalar_signal(
            time, 
            signals[i],
            color=color,
            ls=ls,
            subplot=subplot,
            title=subplot_title[i],
            xtitle=subplot_xtitle[i],
            ytitle=subplot_ytitle[i],
            xlim=xlim,
            ylim=ylim,
            label=False
            )
        
        # Label the plot.
        plt.setp(smooth, label=plot_diag_params['gen.shotnum'])
               
    ## Set overall title.    
    plt.suptitle(title)
    
    return smooth
  

           
def vme_cust_plot_diagnostic(
        time, 
        signal,
        diag,
        subplot,
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls'],
        ):
    """ Used to make a customized diagnostics of an array of shotnumbers 

    This routine also accepts the subplot command requires the user to
    explicitly think about the location of the subplot and input it carefully.

    There is very little error checking here.    
    
    """
    
    
    if diag_params[diag+'.datatype'] == 'scalar':
        return vme_2d_plot_scalar_signal(
            time, 
            signal,
            color=color,
            ls=ls,
            subplot=subplot,
            title=plot_diag_params[diag + '.title'],
            xtitle=plot_diag_params[diag + '.xtitle'],
            ytitle=plot_diag_params[diag + '.ytitle'],
            xlim=plot_diag_params[diag + '.xlim'],
            ylim=plot_diag_params[diag + '.ylim']
            )
    
    ## If the user sent in a vector diagnostic w/o specifying the subplot
    if diag_params[diag+'.datatype'] == 'vector':
        return vme_2d_plot_vector_signal(
            time, 
            signal,
            color=color,
            ls=ls,
            subplot=subplot,
            title=plot_diag_params[diag + '.title'],
            subplot_title=plot_diag_params[diag + '.subplot.titles'],
            subplot_xtitle=plot_diag_params[diag + '.subplot.xtitles'],
            subplot_ytitle=plot_diag_params[diag + '.subplot.ytitles'],
            xlim=plot_diag_params[diag + '.xlim'],
            ylim=plot_diag_params[diag + '.ylim']
            )
            
            
def vme_plot_diagnostic(
        time, 
        signal,
        diag,
        color=plot_diag_params['gen.color'],
        ls=plot_diag_params['gen.ls'],
        ):
    """ Plots diagnostics of an array using generic parameters """
    
    
    vme_cust_plot_diagnostic(time, signal, diag,        
        subplot=plot_diag_params[diag + '.subplot.styles'], color=color, ls=ls)