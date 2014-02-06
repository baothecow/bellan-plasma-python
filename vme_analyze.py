""" A collection of data analysis functions

    vme_avg_scalar_sig: Averages VME data given a list of shots 
        associated with a scalar diagnostic.
        
    get_diag_constructor: Constructs the proper file name for a given data type.
        
    vme_avg_sig_correlation: Correlates an avg signal with the signals stored 
        in signals dict
    
    vme_remove_transients: Some VME ports have large transients compared to others.  This
        function helps to remove those transients.
    

"""


import idl_support as idlsup
import numpy as np
from parameters import diag_params
from file_io_lib import readVME
from cookb_signalsmooth import smooth

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
            
        # Remove transients.
        signal = vme_remove_transients(signal)
        
        # If pre-smooth is activated, it smooth the VME input.
        if (diag_params['gen.presmooth']):
            signal = smooth(signal, diag_params['gen.presmooth.const'])
        
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
        diag_params[diag+'.ind'] = diag_params[diag+'.'+component+'.ind']
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
                                  (signals[shotnum])[low_ind: high_ind])
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
    
    

def get_b_from_hall(signal, sensor='A'):
    """ Use Auna's matrix method to calculate the magnetic field 
    
    hall: list of 3 1d arrays corresponding to hall_x, hall_y, and hall_z
    
    """

    calibration_matrix = get_hall_calibration_matrix(sensor)
    
    return np.dot(calibration_matrix, signal)
    
def get_hall_calibration_matrix(sensor):
    if sensor == 'A': 
        return [[0.0780625, -0.00390558, 0.00189126], [-0.000338635, 0.0876258, -0.000521402], [0.00361111, 0.00381362, 0.0860203]]
    if sensor == 'B':
        return [[0.0829776, -0.00337371, 0.00172883], [0.00353229, 0.0868474, -0.00203384], [0.00109795, 0.00886673, 0.0836279]]
    if sensor == 'C':
        return [[0.0835019, 0.00166185, 0.00697365], [-0.00151638, 0.0906578, -0.00237361], [0.00210450, 0.00484992, 0.0845391]]
    if sensor == 'D':
        return [[0.0834475, -0.00148635, -0.00390268], [0.00917581, 0.0783704, -0.505646e-005], [0.0170444, -0.000291056, 0.0821908]]
    if sensor == 'E':
        return [[0.0896002, -0.00723647, -0.00446408], [0.00451907, 0.0859051, 0.00257616], [0.00530865, 0.00425686, 0.0846567]]
    if sensor == 'F':
        return [[0.0855627, 0.000342191, -0.000336037], [0.00682840, 0.0817025, 0.000688643], [0.00186146, 0.00246870, 0.0822300]]
    else:
        print 'Calibration matrix not found for sensor.  Returning identity'
        return np.identity(3)

    
def mpa_polarity_fix(bx, by, bz):
    """ Corrects for polarity due to mistakes in wiring/labeling/etc"""
    ## In our case, bx and by components are backwards.
    return (-1 * bx, -1 * by, bz)



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
            a = a + [vme_get_breakdown_time(shotnum[0])]
        elif isinstance(shotnum, str):
            a = a + [vme_get_breakdown_time(shotnum)]   
    return a
        

def vme_get_breakdown_time(shotnum):
    """ Extracts breakdown time (in us) from optical trigger data. """
      
    # If shotnum is actually a list, extract the first element.
    if isinstance(shotnum, list):
        print 'list is here'
        shotnum = shotnum[0]
    
    # Sets start and end window (in microseconds to look for the breakdown time)
    START_WINDOW = 10
    END_WINDOW = 18

    # Looks largest rising peak.  Can change the diagnostics to look at to be
    # the tek_hv, iso_hv, or the collimator.
    diag = 'iso_hv'
    filepath = vme_get_filepath(shotnum, diag)
    data = readVME(filepath, cols=diag_params[diag+'.cols'], 
                   rows=diag_params[diag+'.rows'])
                   
    time = list(data[0])
    start_index = time.index(START_WINDOW)
    end_index = time.index(END_WINDOW)
    
    ## Get the diff for points within the window.
    diff = list(np.diff(data[1][start_index:end_index]))
    
    # Get the index of the largest diff value.
    max_ind = diff.index(np.max(diff))
    
    # Return the time associated with that index.
    return data[0][start_index + max_ind]    


def vme_get_shot_peak_time_and_value(shots_array, diag):
    """ Takes in arrays of arrays containing strings of shotnumbers
        Example: [['123', '124'], ['125', '126'], ['127']]. 
        
        Returns a list.  Every odd value is a time, and every even value is a signal.
        
    """
    
    peak_times = []
    peak_values = []
        
    for i in range(0, len(shots_array)):
        data = vme_avg_sig(shots_array[i], diag)
        time = vme_get_time_from_data(data, diag)
        signal = vme_get_signal_from_data(data, diag)
        (peak_time, peak_value) = vme_get_peak_time_and_value(time, signal)
        peak_times = peak_times + [peak_time]
        peak_values = peak_values + [peak_value]
        
    return (peak_times, peak_values)

def vme_unflatten_list(flat_list):
    """ Takes a flat list like [1, 2, 3] and turns it into [[1], [2], [3]] """
    
    flat_list_arr = np.array(flat_list)
    reshaped_arr = flat_list_arr.reshape(-1, 1)
    unflattened_list = reshaped_arr.tolist()
    
    return unflattened_list


def vme_get_peak_time_and_value(time, signal):
    """ Returns the time and value of the peak """
    
    peak_index = vme_get_peak_index(signal)        
    return (time[peak_index], signal[peak_index])
    
def vme_get_peak_index(signal):
    """ Return the index of the peak value in a signal """
    
    max_index = np.where(np.abs(signal) == np.max(np.abs(signal)))
    return max_index[0][0]  # Returns the first value if there are multiple peaks.


def vme_get_filepath(shotnum, diag):
    """ Get path of a given shotnumber and diagnostic """
    
    ## Determine which experiment is associated with the path.    
    idlsup.initialize_exp(shotnum)    
    
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
        
def vme_remove_transients(signal):
    """ A collection of hot patches to deal with transients """
    # Test #1: See if there is a large spike at the beginning compared to the end.
    # If the mean of the points test range are over 10x as large
    # as the last points in test_range, set them to the average of the next 50
    # points after the test range.
    # Relevance: Hall sensor Bx data for one of the VME ports.
    
    test_range = 50
    factor = 10
    
    if (abs(np.mean(signal[0:test_range])) / abs(np.mean(signal[-1*test_range:-1])) > factor):
            signal[0:test_range] = np.mean(signal[test_range+1:test_range+50])
        
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
    if vme_extension == 'hall_bx':
        return '\\shot' + shotnum + 'sensor'+'A'+'_t3ch_n16.dat'
    if vme_extension == 'hall_by':
        return '\\shot' + shotnum + 'sensor'+'A'+'_t3ch_n16.dat'
    if vme_extension == 'hall_bz':
        return '\\shot' + shotnum + 'sensor'+'A'+'_t3ch_n16.dat'






