# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:05:36 2014

@author: bao
"""

import array as ar
import numpy as np
import matplotlib.pyplot as plt
import os
from cookb_signalsmooth import smooth


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


def generate_hall_filepath(shotnum, sensor, basepath=''):
    """
    >> generate_hall_filepath(222, 'A'):
    'E:\\data\\singleloop\\singleloop_VME\\hall\\2014.01.14\\shot222A_t3ch_n16.dat'
    """
    if basepath == '':  # Default basepath
        if os.sep == '/':
            basepath = '/E'
        if os.sep == '\\':
            basepath = 'E:'
        basepath = basepath + os.sep + 'data' + os.sep + 'singleloop' + os.sep + 'singleloop_VME' + os.sep + 'hall' + os.sep
    
    return basepath +get_hall_date(shotnum) + os.sep + 'shot' + str(shotnum) + 'sensor' +  sensor + '_t3ch_n16.dat'


def read_hall_file(filepath):
    """
    Input: path to hall sensor file.
    Output: struct of the location of the sensor and the data captured by that sensor.
    
    See read_hall_position and read_hall_data for appropriate usage examples.
    """
    
    n = 16
    points = 2**n
    num_channel = 4
    
    fin = open(filepath,'rb')
    
    location = ar.array('f')
    location.fromfile(fin, 3)

    array = ar.array('f')
    array.fromfile(fin, num_channel*points)    
    data = np.reshape(array, (num_channel, -1))
    
    return (location, data)
    
def read_hall_position(filepath):
    """ 
    Returns the location of the hall sensor that is stored within the binary file as a 1x3 array.
    
    >>path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\2014.07.24\\shot561sensorE_t3ch_n16.dat'
    >>read_hall_position(path)
    
    array('f', [-1.0, -2.0, 3.0])
    
    """
    return read_hall_file(filepath)[0]

def read_hall_data(filepath):
    """ 
    Returns the data stored within the hall sensor file.  It will be a float array of dimensions 4 x 65536.
    The rows correspond to time, bx, by, bz respectively.

    >>path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\2014.07.24\\shot561sensorE_t3ch_n16.dat'
    >>data = read_hall_data(path)
    >>bx = data[1]
    >>np.shape(bx)
    
    (65536,)
    
    """
    return read_hall_file(filepath)[1]
    
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
    
    
    
    
sensor_locations = list()
    
shot_range = range(303, 463)  # Takes 14 seconds to run.  I should save output to fiele.
#shot_range = range(303, 307)
sensor = 'A'

shot = 303

foo = trim_hall_data(read_hall_data(generate_hall_filepath(shot, sensor)))
bar = read_hall_data(generate_hall_filepath(shot, sensor))

print np.shape(foo)
print np.shape(bar)

plt.plot(bar[0], bar[1])
plt.plot(foo[0], foo[1])


#for shot in shot_range:
#    sensor_locations.append(read_hall_position(generate_hall_filepath(shot, sensor)))
    
    
    

#print sensor_locations    

#
#path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\2014.07.24\\'
#
#filepath = path + 'shot547sensorB_t3ch_n16.dat'
#
#
#
#data = read_hall_data(filepath)
#
#plt.plot(data[0], data[1])
#plt.plot(data[0], data[2])