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
        color_counter=0,
        style_counter=0,
        title=plot_diag_params['gen.title'],
        xtitle=plot_diag_params['gen.xtitle'],
        ytitle=plot_diag_params['gen.ytitle'],
        xlim=plot_diag_params['gen.xlim'],
        ylim=plot_diag_params['gen.ylim'],
        linewidth=1,
        smooth_win=50):
    """ Basic 2D plotting of a single quantity vs time """
    

    plot_style = color_array[color_counter] + style_array[style_counter]

    ## Plot the raw version using a thin line. 
    plt.plot(time, signal, plot_style, linewidth=plotting_vars['thin_ln_width'])
    ## Plot the smoothed version using a thicker line.
    plt.plot(time, smooth(signal, window_len=smooth_win), plot_style,
             linewidth=plotting_vars['thick_ln_width'])
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.xlim(xlim)
    plt.ylim(ylim)



  

def vme_plot_diagnostic(
        time, 
        signal,
        diag='current'):
    """ Plots diagnostics of an array of shotnumbers """
    
    return vme_basic_2d_plot(
        time, 
        signal,
        title=plot_diag_params[diag + '.title'],
        xtitle=plot_diag_params[diag + '.xtitle'],
        ytitle=plot_diag_params[diag + '.ytitle'],
        xlim=plot_diag_params[diag + '.xlim'],
        ylim=plot_diag_params[diag + '.ylim'],
        smooth_win=plot_diag_params[diag + '.smooth_win']        
        )
    

### Some colors and styles.

color_array = ['r', 'b', 'g', 'c', 'm', 'y', 'k']
style_array = ['-', '--', '-', '-', '-', '-', '-']


### A dict of common plotting variables.
plotting_vars = {
    'title': 'Generic plot title',
    'xlim': (10, 30),
    'ylim': (-40, 40),
    'xlim1': (10, 30),
    'ylim1': (-40, 40),
    'xlim2': (10, 30),
    'ylim2': (-40, 40),
    'xtitle': 'Time ('+'$\mu$'+'s)',
    'ytitle': 'Signal',
    'shotnum': '-99',
    'smooth_win': 50,
    'color': 'r',
    'style': '-',
    'thin_ln_width': .5,
    'thick_ln_width': 2
}
    
 




## Obsolete
### Basic 2D plot of signal vs time.
#def vme_basic_2d_plot_from_dict(
#        time,
#        signal, 
#        ):
#    """ Basic 2D plotting of a single quantity vs time """
#
#    plot_style = plotting_vars['color'] + plotting_vars['style']
#
#    ## Plot the raw version using a thin line. 
#    plt.plot(time, signal, plot_style, linewidth=0.5)
#    ## Plot the smoothed version using a thicker line.
#    plt.plot(time, smooth(signal,
#             window_len=plotting_vars['smooth_win']), plot_style,
#             linewidth=2)
#    plt.title(plotting_vars['title'])
#    plt.ylabel(plotting_vars['ytitle'])
#    plt.xlabel(plotting_vars['xtitle'])
#    plt.xlim(plotting_vars['xlim'])
#    plt.ylim(plotting_vars['ylim'])