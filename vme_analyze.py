""" A collection of data analysis functions

    vme_avg_scalar_sig: Averages VME data given a list of shots 
        associated with a scalar diagnostic.
        
    get_diag_constructor: Constructs the proper file name for a given data type.
        
    vme_avg_sig_correlation: Correlates an avg signal with the signals stored 
    in signals dict
    

"""


import idl_support as idlsup
import numpy as np
from parameters import diag_params
from file_io_lib import readVME

def vme_avg_scalar_sig(shotnums, diag):
    """ Averages the VME data associated with several shots 
    
        See vme_avg_sig for input description.
        
        returns a list of 2 1d arrays with the time and the signal average.
    """    
    # Storage array of all the signal.
    signal_sum = np.zeros(diag_params[diag+'.cols'])
    
    # If shotnums is a single string, turn it into a list eg '847' -> ['847']
    if isinstance(shotnums, basestring):
        shotnums = [shotnums]
        
    # Temp holder dict for signals.
    signals = {}
    
    ## Loop through and sum the data up.
    for shotnum in shotnums:
        filepath = vme_get_filepath(shotnum, diag)
        data = readVME(filepath, cols=diag_params[diag+'.cols'], 
                       rows=diag_params[diag+'.rows'])
        time = data[0, :]
        signal = data[diag_params[diag+'.ind'], :] 
        ## Subtract off any dc offset from the first 100 points of the signal.
        signals[shotnum] = signal - np.mean(signal[0:100])
        signal_sum = np.add(signals[shotnum], signal_sum)
    avg_signal = np.divide(signal_sum, np.size(shotnums))
    
    ## Checks the correlation between the different signals to check for VME
    ## failures or obvious bad data.
    vme_avg_sig_correlation(avg_signal, signals, diag)
    
    return (time, avg_signal)
    
def vme_avg_vector_sig(shotnums, diag='sol_mpa'):
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
        diag_params[diag+'.ind'] = diag_params['gen.probenum']
        diag_params[diag+'.vme'] = diag + '_' + component
        avg_data = vme_avg_scalar_sig(shotnums, diag)
        probe_data['time'] = avg_data[0]
        probe_data[component] = avg_data[1]
        
    return probe_data
    
def vme_avg_sig_correlation(avg_signal, signals, diag):
    """ Correlates an avg signal with the signals stored in signals dict
    
    Input:  avg_signal: 1-D array of the average signal.
            signals: dict containing all the relevant shot signals.
    
    """
    
    SUSPECT_VME_FAILURE_THRESHOLD = .2
    COEFF_INDEX = (0,1)
    
    diag_ = diag_params[diag+'.vme']
    corr_threshold = diag_params[diag+'.corr.threshold']
    low_ind = diag_params['gen.corr.lower.ind']
    high_ind = diag_params['gen.corr.upper.ind']
    
    for shotnum in signals.keys():
        # Gets a 2x2 correlation matrix between the average signal and each ind signal.
        corr_matrix = np.corrcoef(avg_signal[low_ind: high_ind], 
                                  signals[shotnum][low_ind: high_ind])
        if corr_matrix[COEFF_INDEX] < SUSPECT_VME_FAILURE_THRESHOLD:
            print 'Suspect VME failure for ' + diag_ + ' in shotnum: ' + shotnum
        ## Crude implementation of comparing a shot to its peers.
        elif corr_matrix[COEFF_INDEX] < corr_threshold:
            print diag_ + ' for shotnum: ' + shotnum + ' may be different from its peers'
    

def get_b_from_bdot(time, bdot):
    """ Converts a bdot signal matrix back into magnetic field matrix 
    
    Currently employing Carlo's method.  May switch to Auna's method in
    the future.
    
    time: 1d time vector.
    bdot: list of 3 1d arrays corresponding to bdot_x, bdot_y, and bdot_z
    
    """
    
    TESLA_TO_GAUSS = 1.0e4
    
    ## Average value of turns*area.
    na = 1.0e-4
    
    bdot_x = bdot[0]
    bdot_y = bdot[1]
    bdot_z = bdot[2]
    
    dt = 1e-6 * time[1]-time[0]
    
    bx = -1*np.multiply(integrate(dt, bdot_x), (TESLA_TO_GAUSS/na))
    by = -1*np.multiply(integrate(dt, bdot_y), (TESLA_TO_GAUSS/na))
    bz = -1*np.multiply(integrate(dt, bdot_z), (TESLA_TO_GAUSS/na))
    
    return mpa_polarity_fix(bx, by, bz)         # Correct for polarity.
    
    
def mpa_polarity_fix(bx, by, bz):
    """ Corrects for polarity due to mistakes in wiring/labeling/etc"""
    ## In our case, by and bz components are backwards.
    return (-1 * bx, by, -1 * bz)



def integrate(dt, signal):
    """ Use cumsum and trapezoid rule to integrate a signal with unif spacing """
    cumsum = np.cumsum(signal)
    foo = np.subtract(np.subtract(np.multiply(cumsum, 2), signal), signal[0])
    return np.multiply(foo, dt/2.)


def vme_get_breakdown_times(shotnums):
    """ Extract breakdown time of an array of shots """
    a = []    
    for shotnum in shotnums:
        if isinstance(shotnum, list):
            print 'hello'
            a = a + [vme_get_breakdown_times(shotnum)]
        elif isinstance(shotnum, str):
            print 'hi'
            a = a + [vme_get_breakdown_time(shotnum)]   
    return a
        

def vme_get_breakdown_time(shotnum):
    """ Extracts breakdown time (in us) from optical trigger data. """
    
    # If shotnum is actually a list, extract the first element.
    if isinstance(shotnum, list):
        shotnum = shotnum[0]
    
    # Sets the number of points to ignore.  May help with noise.
    IGNORE_PTS = 500

    diag = 'collimator'
    filepath = vme_get_filepath(shotnum, diag)
    data = readVME(filepath, cols=diag_params[diag+'.cols'], 
                   rows=diag_params[diag+'.rows'])
                   
    ## Get the diff between points while ignoring the first 500 points.
    diff = list(np.diff(data[1][IGNORE_PTS:]))
    
    # Get the index of the largest diff value.
    max_ind = diff.index(np.max(diff))
    
    # Return the time assocaited with that index.
    return data[0][IGNORE_PTS + max_ind]    
   
    
def vme_get_filepath(shotnum, diag):
    """ Get path of a given shotnumber and diagnostic """
    
    root = idlsup.get_idl_vme_path()
    constructor = get_diag_constructor(shotnum, diag_params[diag+'.vme'])
    return root + idlsup.get_shot_date(shotnum) + constructor    

    
def vme_get_time_from_data(data, diag):
    """ extracts time from data from vme_avg_sig """
    if diag_params[diag+'.datatype'] == 'scalar':
        return data[0]
    if diag_params[diag+'.datatype'] == 'vector':
        return data['time']
        
def vme_get_signal_from_data(data, diag):
    """ extracts sgnal from data from vme_avg_sig 

    if scalar, returns a 1-D array.
    if vector, returns a list of arrays correspondong to each component.
    
    """
    if diag_params[diag+'.datatype'] == 'scalar':
        return data[1]
    if diag_params[diag+'.datatype'] == 'vector':
        signal = list()        
        for component in diag_params[diag + '.components']:
            signal.append(data[component])       
        return signal
        
    
    
def vme_avg_sig(shotnums, diag):
    """ Averages the VME data associated with several shots 
    
        shotnums: a list of strings denoting shot numbers eg ['525', '526', '571']
        diag:   string denoting the wanted diagnostics.
                    * 'current' is rogowski coil current.
                    * 'tek_hv' is Tektronic high voltage'
                    * 'iso_hv' is Xiang's high voltage probe
        
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
    
    if vme_extension == 'current' or vme_extension == 'tek_hv':
        return '\\vi_t2ch13_' + shotnum + '.dat'
    if vme_extension == 'iso_hv':
        return '\\HV_' + shotnum + '.dat'
    if vme_extension == 'sol_mpa_bx':
        return '\\bx_4x16384_' + shotnum + '.dat'
    if vme_extension == 'sol_mpa_by':
        return '\\by_4x16384_' + shotnum + '.dat'
    if vme_extension == 'sol_mpa_bz':
        return '\\bz_4x16384_' + shotnum + '.dat'
    if vme_extension == 'optical_trigger':
        return '\\optical_trigger_t1ch13_' + shotnum + '.dat'    







