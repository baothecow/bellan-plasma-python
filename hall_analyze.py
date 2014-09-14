# -*- coding: utf-8 -*-
"""
Created on Fri Sep 12 11:05:36 2014

@author: bao
"""

import array as ar
import numpy as np
import matplotlib.pyplot as plt
import os
from file_io_lib import pickle_read, pickle_dump
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
    

    
def get_calibration_matrix(sensor):
    """ Returns a calibration matrix """
    if sensor == 'A':
        return [[0.0780625, -0.00390558, 0.00189126], [-0.000338635, 0.0876258, -0.000521402], [0.00361111, 0.00381362, 0.0860203]] # sensor/board: A/A
    elif sensor == 'B':
        return [[0.0829776, -0.00337371, 0.00172883], [0.00353229, 0.0868474, -0.00203384], [0.00109795, 0.00886673, 0.0836279]] # sensor/board: B/B
    elif sensor == 'C':
        return [[0.0835019, 0.00166185, 0.00697365], [-0.00151638, 0.0906578, -0.00237361], [0.00210450, 0.00484992, 0.0845391]] # sensor/board: C/C
    elif sensor == 'D':
        return [[0.0834475, -0.00148635, -0.00390268], [0.00917581, 0.0783704, -0.505646e-005], [0.0170444, -0.000291056, 0.0821908]] # sensor/board: D/D
    elif sensor == 'E':
        return [[0.0896002, -0.00723647, -0.00446408], [0.00451907, 0.0859051, 0.00257616], [0.00530865, 0.00425686, 0.0846567]] # sensor/board: E/E
    elif sensor == 'F':
        return [[0.0855627, 0.000342191, -0.000336037], [0.00682840, 0.0817025, 0.000688643], [0.00186146, 0.00246870, 0.0822300]] # sensor/board: F/F
    else:
        print 'Uncalibrated sensor or sensor does not exist!'
        return [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
def get_polarity_matrix(x, y, z):
    """
    Input: a -1 or 1 for x, y, and z which corresponds to whether the setup's x, y, or z axis aligns with or is anti-parallel to the sensor axis.
    Output: A 3x3 calibration matrix that corrects for polarity.
    """
    return [[x, 0, 0], [0, y, 0], [0, 0, z]]
    
def calc_hall_for_shots(shotnums, sensor, polarization = [-1, -1, -1]):
    """
    
    """

    location_list = list()
    data_list = list()

    # Perform the calculations and save to file.
    for shot in shotnums:
        location_list.append(read_hall_position(generate_hall_filepath(shot, sensor)))
        foo = trim_hall_data(read_hall_data(generate_hall_filepath(shot, sensor)))
        cal_matrix = get_calibration_matrix(sensor)
        pol_matrix = get_polarity_matrix(polarization[0], polarization[1], polarization[2])
        B = np.dot(cal_matrix, np.dot(pol_matrix, foo[1:4]))
        data_list.append(np.concatenate((foo[0:1], B[0:3]), axis=0))
        
    return (location_list, data_list)
    
    
def save_hall_to_file(location_list, data_list, path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\'):
    """ Save the data to file temporariliy """
    
    filename = 'location.pickle'
    datafn = 'data.pickle'
       
    pickle_dump(location_list, filename, path)
    pickle_dump(data_list, datafn, path)
    
def read_hall_for_shots_from_file(path):
    
    
    location = pickle_read(path + 'location.pickle')
    data_list = pickle_read(path + 'data.pickle')
    
    return (location, data_list)
        
    

sensor = 'A'
start = 358
shot_range = range(start, start+10)




(location_list, data_list) = calc_hall_for_shots(shot_range, sensor)
save_hall_to_file(location_list, data_list)



path = 'E:\\data\\singleloop\\singleloop_VME\\hall\\'
(location_list, data_list) = read_hall_for_shots_from_file(path)

plt.figure()

for data in data_list:
    plt.plot(data[0], data[1], 'g')
    plt.plot(data[0], data[2], 'b')
    plt.plot(data[0], data[3], 'r')

print np.array(location_list)
    
    
#sensor_locations = list()
#    
#shot_range = range(303, 463)  # Takes 14 seconds to run.  I should save output to fiele.
##shot_range = range(303, 307)
#sensor = 'A'
#
#shot = 320
#
#location = read_hall_position(generate_hall_filepath(shot, sensor))
#foo = trim_hall_data(read_hall_data(generate_hall_filepath(shot, sensor)))
#
#cal_matrix = get_calibration_matrix(sensor)
#pol_matrix = get_polarity_matrix(-1, -1, -1)
#
#bar = np.dot(cal_matrix, np.dot(pol_matrix, foo[1:4]))
#
#
#print location






#plt.plot(foo[0], foo[1], 'g')  #x 
#plt.plot(foo[0], foo[2], 'b')  #y
#plt.plot(foo[0], foo[3], 'r')  #z


#plt.plot(foo[0], bar[0], 'g')  #x 
#plt.plot(foo[0], bar[1], 'b')  #y
#plt.plot(foo[0], bar[2], 'r')  #z



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