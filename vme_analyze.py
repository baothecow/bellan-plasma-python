""" A collection of data analysis functions

    vme_avg_sig:    Averages VME data given a list of shots.
    get_diag_constructor:   Constructs the proper file name for a given data
        type.
    

"""


import idl_support as idlsup
import numpy as np
from parameters import diag_params
from file_io_lib import readVME

import matplotlib.pyplot as plt

def vme_avg_sig(shotnums, diag='current', smoothing_constant=50):
    """ Averages the VME data associated with several shots 
    
        shot:   a list of strings denoting shot numbers eg ('525', '526', '571')
        diag:   string denoting the wanted diagnostics.
                    * 'current' is rogowski coil current.
                    * 'tek_hv' is Tektronic high voltage'
                    * 'iso_hv' is Xiang's high voltage probe
        smoothing_constant: Smoothing to be used.
        
        returns an list of 2 1d arrays with the time and the signal average.
    """ 
    root = idlsup.get_idl_vme_path()
    
    # Storage array of all the signal.
    signal_sum = np.zeros(diag_params[diag+'.cols'])
    
    # If shotnums is a single string, turn it into a list eg '847' -> ['847']
    if isinstance(shotnums, basestring):
        shotnums = [shotnums]
    
    ## Loop through and sum the data up.
    for shotnum in shotnums:
        constructor = get_diag_constructor(shotnum, diag_params[diag+'.vme'])
        filename = root + idlsup.get_shot_date(shotnum) + constructor
        data = readVME(filename, cols=diag_params[diag+'.cols'], 
                       rows=diag_params[diag+'.rows'])
        time = data[0, :]
        signal = data[diag_params[diag+'.ind'], :] 
        signal_sum = np.add(signal, signal_sum)
    avg_signal = np.divide(signal_sum, np.size(shotnums))
    
    return (time, avg_signal)
    
def vme_avg_mpa_probe(shotnums, diag='sol_mpa', probenum=1, smoothing_constant=50):
    """ Averages the VME magnetic probe data associated with user inputted shots
    
        This function specializes in tricky diagnostics with multiple axes
        and multiple probes.
    
        shot:   a list of strings denoting shot numbers eg ('525', '526', '571')
        diag:   string denoting the wanted diagnostics.
                    * 'sol_mpa' is solar_mpa
        
        probe:  probe number to be returned.

        smoothing_constant: Smoothing to be used.
        
        return a dictinoary of 4 1-d arrays (time, bx, by, bz) for the desired probe.
    """ 
     
    probe_data = {}  
    
    ## Loop through the components of the diagnostics.  Ex: bx, by, bz
    for component in diag_params[diag+'.components']:
    ## Loop through and sum the data up.
        # Set up the appropriate probe num.
        diag_params[diag+'.ind'] = probenum
        diag_params[diag+'.vme'] = diag + '_' + component
        avg_data = vme_avg_sig(shotnums, diag=diag)
        plt.plot(avg_data[0], avg_data[1])
        probe_data['time'] = avg_data[0]
        probe_data[component] = avg_data[1]
        
    return probe_data
    
        
def get_diag_constructor(shotnum, vme_extension):
    """ Construct the filename for a specific diagnostics """
    
    if vme_extension == 'iv':
        return '\\vi_t2ch13_' + shotnum + '.dat'
    if vme_extension == 'HV':
        return '\\HV_' + shotnum + '.dat'
    if vme_extension == 'sol_mpa_bx':
        return '\\bx_4x16384_' + shotnum + '.dat'
    if vme_extension == 'sol_mpa_by':
        return '\\by_4x16384_' + shotnum + '.dat'
    if vme_extension == 'sol_mpa_bz':
        return '\\bz_4x16384_' + shotnum + '.dat'







