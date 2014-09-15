# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:05:36 2014




Note: There is already a method of reading Hall sensor data from vme_analyze but does
not intepret the location of the hall sensors and thus introduces artificial transients
which are then removed.

It also doesn't use a polarization matrix.


@author: bao
"""

import array as ar
import numpy as np
import matplotlib.pyplot as plt
import os
from file_io_lib import pickle_read, pickle_dump
from cookb_signalsmooth import smooth
from vme_analyze import get_hall_calibration_matrix
from parameters import exp_paths


def get_all_file_paths_in_folder_and_subfolder(folderpath):
    """ 
    Function will check a root folder and return a list containing paths to all the
    files in that folder 
    
    >>> folderpath = 'E:\\'
    >>> get_all_file_paths_in_folder_and_subfolder(folderpath)
    
    Output: a list of paths to every file in the folder and its subfolders.
    
    """
    path_list = list()
    for path, subdirs, files in os.walk(folderpath):
        for name in files:
            path_list.append(os.path.join(path, name))
    return path_list


def get_hall_date(shotnum):
    """ Returns the data for a given shot number """
    if shotnum >= 514 and shotnum <= 563:
        return '2014.07.24'
    if shotnum >= 463 and shotnum <= 513:
        return '2014.07.23'
    if shotnum >= 303 and shotnum <= 462:
        return '2014.04.01'
    if shotnum >=301 and shotnum <= 302:
        return '2014.03.19'
    if shotnum >= 270 and shotnum <= 300:
        return '2014.01.15'
    if shotnum >= 217 and shotnum <= 269:
        return '2014.01.14'


def generate_hall_filepath(shotnum, sensor, basepath=exp_paths['hall.IDL_VME_PATH'], reduced=False, n=11):
    """
    >> generate_hall_filepath(222, 'A'):
    'E:\\data\\singleloop\\singleloop_VME\\hall\\2014.01.14\\shot222sensorA_t3ch_n16.dat'
    >> generate_hall_filepath(821, 'F', reduced=True, n=14)
    'E:\\data\\singleloop\\singleloop_VME\\hall\\reduced\\shot821sensorF_t3ch_n14.dat'
    """

    if reduced:
        return basepath + 'reduced' + os.sep + 'shot' + str(shotnum) + 'sensor' +  sensor + '_t3ch_n' + str(n) + '.dat'
    else:
        return basepath +get_hall_date(shotnum) + os.sep + 'shot' + str(shotnum) + 'sensor' +  sensor + '_t3ch_n16.dat'


def read_hall_file(filepath, n=16):
    """
    Input: path to hall sensor file.
    Output: struct of the location of the sensor and the data captured by that sensor.
    
    See read_hall_position and read_hall_data for appropriate usage examples.
    
    Note: If n=16, the assumption is that this is the IDL hall file which has 3 numbers
    representation location data.
    """
    
    num_channel = 4
    
    fin = open(filepath,'rb')    
    
    #if n==16:
        # Have to use this roundable method to get the first 3 points.
    location = ar.array('f')
    location.fromfile(fin, 3)

    # Read in the regular data.
    data = np.reshape(np.fromfile(fin, dtype=np.float32), (num_channel, -1))
    
    fin.close()
    
    return (location, data)
        
    
def read_hall_position(filepath, n=16):
    """ 
    Returns the location of the hall sensor that is stored within the binary file as a 1x3 array.
    
    >>path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\2014.07.24\\shot561sensorE_t3ch_n16.dat'
    >>read_hall_position(path)
    
    array('f', [-1.0, -2.0, 3.0])
    
    """
    return read_hall_file(filepath, n=n)[0]

def read_hall_data(filepath, n=16):
    """ 
    Returns the data stored within the hall sensor file.  It will be a float array of dimensions 4 x 65536.
    The rows correspond to time, bx, by, bz respectively.

    >>path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\2014.07.24\\shot561sensorE_t3ch_n16.dat'
    >>data = read_hall_data(path)
    >>bx = data[1]
    >>np.shape(bx)
    
    (65536,)
    
    """
    return read_hall_file(filepath, n=n)[1]
    
    

    
def reduce_hall_data(folderpath, output_path = exp_paths['hall.IDL_VME_PATH'] + 'reduced' + os.sep, ntrim=5):
    """
    Use trim_hall_data to smooth and trim the hall data files.  Remove the location numbers and output them as reduced files.
    
    Input: The folder containing the relevant hall data.
    """
    
    all_paths = get_all_file_paths_in_folder_and_subfolder(folderpath)
    
    for path in all_paths:
        filename = os.path.splitext(os.path.basename(path))[0]  # Extract the file name and remove the extension..
        if filename[0:4] == 'shot':
            (location, data) = read_hall_file(path)
            trimmed_data = np.array(trim_hall_data(data, ntrim=ntrim), dtype=np.float32)
            new_filename = filename[0:-3] + 'n' + str(16-ntrim) + '.dat' # Generate new filename.            
            if os.path.exists(output_path + new_filename):
                print 'Warning! ' + new_filename + ' already exists.  Delete first before reducing.'
            else:
                write_reduced_data(output_path + new_filename, location, trimmed_data)
    
    
    
def trim_hall_data(data, ntrim=5):
    """
    Hall sensor data is 2^16 points.  This is overkill.  This method's role is to trim this.
    
    By default, It will do a 2^5 point smoothing and keep every other 2^5 points
    """
    
    SMOOTHING_CONST = 2**5
    
    # Wrapper function to use smooth function with np.apply_along_axis
    def smooth_wrapper(smooth_ftn, SMOOTHING_CONST):
        def smooth(array_1d):
            return smooth_ftn(array_1d, SMOOTHING_CONST)
        return smooth
        
    my_smooth = smooth_wrapper(smooth, SMOOTHING_CONST)
    
    # Applys the appropriate smoothing and return every other 2**ntrim points of the array column.
    return np.apply_along_axis(my_smooth, 1, data)[:, 1::2**ntrim]
    
        
def get_polarity_matrix(x, y, z):
    """
    Input: a -1 or 1 for x, y, and z which corresponds to whether the setup's x, y, or z axis aligns with or is anti-parallel to the sensor axis.
    Output: A 3x3 calibration matrix that corrects for polarity.
    """
    return [[x, 0, 0], [0, y, 0], [0, 0, z]]
    
def calc_hall_for_shots(shotnums, sensor, polarization = [-1, 1, -1], n=11):
    """
    Function may be obsolete soon.
    """

    location_list = list()
    data_list = list()

    # Perform the calculations and save to file.
    for shot in shotnums:
        location_list.append(read_hall_position(generate_hall_filepath(shot, sensor)))
        foo = trim_hall_data(read_hall_data(generate_hall_filepath(shot, sensor)))
        cal_matrix = get_hall_calibration_matrix(sensor)
        pol_matrix = get_polarity_matrix(polarization[0], polarization[1], polarization[2])
        B = np.dot(cal_matrix, np.dot(pol_matrix, foo[1:4]))
        data_list.append(np.concatenate((foo[0:1], B[0:3]), axis=0))
        
    return (location_list, data_list)
    
def get_b_at_ind_for_shot_sensor(t_ind, shotnum, sensor, polarization = [-1, 1, -1], basepath=exp_paths['hall.IDL_VME_PATH'], reduced=True, n=11):
    if reduced:
        filepath = generate_hall_filepath(shotnum, sensor, reduced=reduced, n=n)
        v_hall = read_hall_data(filepath, n=n)
        cal_matrix = get_hall_calibration_matrix(sensor)
        pol_matrix = get_polarity_matrix(polarization[0], polarization[1], polarization[2])
        B = np.dot(cal_matrix, np.dot(pol_matrix, v_hall[1: 4]))
        return B[:, t_ind]
    else:
        print 'Only reduced paths have been implemented!  Returning [0, 0, 0]'
        return [0, 0, 0]

def get_loc_for_shot_sensor(shotnum, sensor, basepath=exp_paths['hall.IDL_VME_PATH'], reduced=True, n=11):
    if reduced:
        filepath = generate_hall_filepath(shotnum, sensor, reduced=reduced, n=n)
        return read_hall_position(filepath, n=n)
    else:
        print 'Only reduced paths have been implemented!  Returning [0, 0, 0]'
        return [0, 0, 0]
    
    

    
    
def correct_hall_location(shotnum, sensor, location, basepath=exp_paths['hall.IDL_VME_PATH']):
    """
    Input: shotnum (integer), sensor (string), location (list of doubles)
    Output: corrected location value.
    
    >>> correct_hall_location(311, 'A', [0., 4., 2.])
    
    """
    
    filepath = generate_hall_filepath(shotnum, sensor, basepath, reduced=True)
    
    (old_loc, data) = read_hall_file(filepath)
    
    print type(old_loc)    
    
    # Check to make sure the location is a list of 3 elements long.
    if isinstance(location, list) and all([isinstance(x, (int, long, float)) for x in location]) and len(location) == 3:
        print 'Shot ' + str(shotnum) + ': Modifying location from ' + str(old_loc) + ' to ' + str(location)
        write_reduced_data(filepath, ar.array('f', location), data)
    else:
        print 'Error with location input.  No modification done'
        
        
def write_reduced_data(filepath, location, data):
    """
    location -- array of 3 points, x, y, z.
    data -- numpy float32 array.
    """

    fout = open(filepath, 'wb')
    fout.write(location)
    data.tofile(fout)
    fout.close()
    




    
#    
#def save_hall_to_file(location_list, data_list, path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\'):
#    """ Save the data to file temporariliy """
#    
#    filename = 'location.pickle'
#    datafn = 'data.pickle'
#       
#    pickle_dump(location_list, filename, path)
#    pickle_dump(data_list, datafn, path)
#    
#def read_hall_from_file(path):
#    
#    
#    location = pickle_read(path + 'location.pickle')
#    data_list = pickle_read(path + 'data.pickle')
#    
#    return (location, data_list)

