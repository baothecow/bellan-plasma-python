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
        color_counter=0,
        style_counter=0,
        title='2D Signal vs Time',
        xtitle='Time (' + '$\mu$' + 's)',
        ytitle='Signal',
        xlim=[10, 30],
        ylim=[-40, 40],
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


## Basic 2D plot of signal vs time.
def vme_basic_2d_plot_from_dict(
        time,
        signal, 
        ):
    """ Basic 2D plotting of a single quantity vs time """

    plot_style = plotting_vars['color'] + plotting_vars['style']

    ## Plot the raw version using a thin line. 
    plt.plot(time, signal, plot_style, linewidth=0.5)
    ## Plot the smoothed version using a thicker line.
    plt.plot(time, smooth(signal,
             window_len=plotting_vars['smooth_win']), plot_style,
             linewidth=2)
    plt.title(plotting_vars['title'])
    plt.ylabel(plotting_vars['ytitle'])
    plt.xlabel(plotting_vars['xtitle'])
    plt.xlim(plotting_vars['xlim'])
    plt.ylim(plotting_vars['ylim'])

## Plot of two signals with common time axis.
def vme_2params_2d_plot(
        time,
        signal_1,
        signal_2,
        color_counter=0,            
        style_counter=0,
        title='2D Plot vs Time',
        xtitle1='Time (' + '$\mu$' + 's)',
        ytitle1='',
        xlim1=[10, 30],
        ylim1=[-40, 40],
        smooth_win_1=50,
        xtitle2='Time (' + '$\mu$' + 's)',
        ytitle2='',
        xlim2=[10, 30],
        ylim2=[-40, 40],
        smooth_win_2=50):
    """ 2D Plot of two signals with common time axis. """

    ## Generate the two subplot by calling the basic plot function for
    ## each subplot.
    plt.subplot(211)
    vme_basic_2d_plot(
        time,
        signal_1,
        color_counter=color_counter,
        style_counter=style_counter,
        xtitle=xtitle1,
        ytitle=ytitle1,
        xlim=xlim1,
        ylim=ylim1,
        smooth_win=smooth_win_1)
    plt.subplot(212)
    vme_basic_2d_plot(
        time,
        signal_2,
        title='',           # Clears out title of lower plot.
        color_counter=color_counter,
        style_counter=style_counter,
        xtitle=xtitle2,
        ytitle=ytitle2,
        xlim=xlim2,
        ylim=ylim2,
        smooth_win=smooth_win_2)

    ## Remove the spacing between the subplots
    subplots_adjust(hspace=0.001)
        


def vme_plot_diagnostic(
        time, 
        signal,
        diag='current'):
    """ Plots diagnostics of an array of shotnumbers """
    
    vme_basic_2d_plot(
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
    
 
plot_diag_params = {
    'current.title': 'Current vs time',
    'current.ytitle': 'Current (kA)',
    'current.xtitle': 'Time (' + '$\mu$' + 's)',
    'current.xlim': [10, 30],
    'current.ylim': [-40, 40],
    'current.smooth_win': 50,
    'tek_hv.title': 'Voltage vs time',
    'tek_hv.ytitle': 'Voltage (V)',
    'tek_hv.xtitle': 'Time (' + '$\mu$' + 's)',
    'tek_hv.xlim': [10, 30],
    'tek_hv.ylim': [-4000, 4000],
    'tek_hv.smooth_win': 50
}     
