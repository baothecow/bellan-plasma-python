""" A collection of data analysis functions

    vme_avg_scalar_sig:    Averages VME data given a list of shots 
                            associated with a scalar diagnostic.
    get_diag_constructor:   Constructs the proper file name for a given data
        type.
    

"""


import idl_support as idlsup
import numpy as np
from parameters import diag_params
from file_io_lib import readVME

def vme_avg_scalar_sig(shotnums, diag='current', smoothing_constant=50):
    """ Averages the VME data associated with several shots 
    
        See vme_avg_sig for input description.
        
        returns a list of 2 1d arrays with the time and the signal average.
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
        ## Subtract off any dc offset from the first 100 points of the signal.
        signal = signal - np.mean(signal[0:100])
        signal_sum = np.add(signal, signal_sum)
    avg_signal = np.divide(signal_sum, np.size(shotnums))
    
    return (time, avg_signal)
    
def vme_avg_vector_sig(shotnums, diag='sol_mpa', probenum=1, smoothing_constant=50):
    """ Averages the VME magnetic probe data associated with user inputted shots
    
        See vme_avg_sig for input description.
        
        return a dict with 1-d arrays corresponding to time and each 
               element in diag.components
    """ 
     
    probe_data = {}  
    
    ## Loop through the components of the diagnostics.  ex: bx, by, bz
    for component in diag_params[diag+'.components']:
    ## Loop through and sum the data up.
        # Set up the appropriate probe num.
        diag_params[diag+'.ind'] = probenum
        diag_params[diag+'.vme'] = diag + '_' + component
        avg_data = vme_avg_scalar_sig(shotnums, diag)
        probe_data['time'] = avg_data[0]
        probe_data[component] = avg_data[1]
        
    return probe_data
    
    
def vme_avg_sig(shotnums, diag='current', smoothing_constant=50):
    """ Averages the VME data associated with several shots 
    
        shot:   a list of strings denoting shot numbers eg ('525', '526', '571')
        diag:   string denoting the wanted diagnostics.
                    * 'current' is rogowski coil current.
                    * 'tek_hv' is Tektronic high voltage'
                    * 'iso_hv' is Xiang's high voltage probe
        smoothing_constant: Smoothing to be used.
        
        returns either:
            * a list of 2 1-d arrays.
            * a dict with 1-d arrays corresponding to time and each 
              element in diag.components
            
    """ 

    if diag_params[diag+'.datatype'] == 'scalar':
        return vme_avg_scalar_sig(shotnums, diag=diag)
    
    if diag_params[diag+'.datatype'] == 'vector':
        return vme_avg_vector_sig(shotnums, diag=diag)

        
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







