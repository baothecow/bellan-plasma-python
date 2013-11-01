""" A collection of data analysis functions

    vme_avg_sig:    Averages VME data given a list of shots.
    get_diag_constructor:   Constructs the proper file name for a given data
        type.
    

"""


import idl_support as idlsup
import numpy as np
from parameters import diag_params
from file_io_lib import readVME


def vme_avg_sig(shotnums, diag='current', smoothing_constant=50):
    """ Averages the VME data associated with several shots 
    
        shot:   a list of strings denoting shot numbers eg ('525', '526', '571')
        diag:   string denoting the wanted diagnostics.
                    * 'current' is rogowski coil current.
                    * 'tek_hv' is Tektronic high voltage'
                    * 'sol_hv' is Xiang's high voltage probe
        smoothing_constant: Smoothing to be used.
        
        returns an 1d array with the signal average.
    """ 
    root = idlsup.get_idl_vme_path()
    
    # Storage array of all the signal.
    signal_sum = np.zeros(diag_params[diag+'.cols'])
    
    # If shotnums is a single string, turn it into a list
    if isinstance(shotnums, basestring):
        shotnums = [shotnums]
    
    ## Loop through and sum the data up.
    for shotnum in shotnums:
        constructor = get_diag_constructor(shotnum, diag_params[diag+'.vme'])
        filename = root + idlsup.get_shot_date(shotnum) + constructor
        data = readVME(filename, rows=diag_params[diag+'.rows'])
        time = data[0, :]
        signal = data[diag_params[diag+'.ind'], :] 
        signal_sum = np.add(signal, signal_sum)
        
    avg_signal = np.divide(signal_sum, np.size(shotnums))
    
    return (time, avg_signal)
    
        
def get_diag_constructor(shotnum, vme_extension):
    """ Construct the filename for a specific diagnostics """
    
    if vme_extension == 'iv':
        return '\\vi_t2ch13_' + shotnum + '.dat'







