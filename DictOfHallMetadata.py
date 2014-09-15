# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 14:09:34 2014

@author: bao
"""

import os as os
import cPickle as pickle
from hall_analyze import read_hall_position
from parameters import exp_paths


## Creating an object which contains breakdown time.
class DictOfHallMetadata:
    """
    Class is a dict which stores the breakdown times.
    
    Stores a dict of (breakdown_time, shotdate)
    
    
    """
    
    def __init__(self, shotnums, descript, root_path=exp_paths['hall.IDL_VME_PATH'], sensor_list = ['A', 'B', 'C', 'D', 'E', 'F'], n=11):
        
        
        self.shotnums = shotnums
        self.descript = descript
        self.root_path = root_path
        self.sensor_list = sensor_list
        self.n = n
        
        self.update_file_path()
        self.initialize_obj()
        
    ### INITIALIZATION FUNCTIONS ###
    
    def update_file_path(self):
        self.file_path = self.root_path + 'metadata' + os.sep + str(self.descript) + '_' + self.get_shot_summary_string() + '.pickle'
        self.reduced_data_folder = self.root_path + 'reduced' + os.sep

    def get_shot_summary_string(self):
        """ 
        Used to generate a summary string given a list of integer shotnumbers.   
        
        >>> shotnums = range(100, 123)
        >>> get_shot_summary_string(shotnums)
        '100_101_102_19_shots_122'
        
        >>> shotnums = [123, 111, 165]
        >>> get_shot_summary_string(shotnums)
        '123_111_165'
        
        """
        numElements = len(self.shotnums)
        num_pre_shots = 3
        summary_string = ""
        
        if numElements <= num_pre_shots + 1:
            for i in range(0, numElements - 1):
                summary_string = summary_string + str(self.shotnums[i]) + "_"
        else:
            for i in range(0, num_pre_shots):
                summary_string = summary_string + str(self.shotnums[i]) + "_"
            summary_string = summary_string  + str(numElements - num_pre_shots - 1) + '_shots_'
                
        summary_string = summary_string + str(self.shotnums[numElements - 1])
        
        return summary_string
    
        
    def check_existence_pickle_file(self):
        return os.path.exists(self.file_path)

    def initialize_obj(self):
        """ Create an empty dict by default.  Populate the dict if a pickle file exists. """
        self.metadata = dict()
        if self.check_existence_pickle_file():
            self.pickle_read()
            
    ### INTERACTIVE FUNCTIONS
            
    def update_location(self):
        """
        Checks to see if reduced data exists for the shot and populates the keys with the existing relationgs.
        """
        for shotnum in self.shotnums:
            for sensor in self.sensor_list:
                reduced_filepath = self.reduced_data_folder + os.sep + 'shot' + str(shotnum) + 'sensor' + sensor + '_t3ch_n' + str(self.n) + '.dat'
                if os.path.exists(reduced_filepath):
                    position = read_hall_position(reduced_filepath, n=self.n)
                    self.metadata[str(shotnum)+'.'+str(sensor)+'.loc'] = [position[0], position[1], position[2]] 
            
        
    def get_location(self, shotnum, sensor):
        if self.metadata.has_key(str(shotnum)+'.'+str(sensor)+'.loc'):
            return self.metadata[str(shotnum)+'.'+str(sensor)+'.loc']
        else:
            print 'No key found for shot: ' + str(shotnum) + ' sensor ' + str(sensor)
            print 'Returning [0, 0, 0]'
            return [0, 0, 0]
        
    def set_location(self, shotnum, sensor, location):
        """
        Example
        >>> set_location(313, 'A', [1, 2, 3])
        """
        self.metadata[str(shotnum)+'.'+str(sensor)+'.loc'] = location
        
        
    def print_all_keys(self):
        for key in self.metadata:
            print (key, self.metadata[key])
            print '--------'

    
    ######### IO FUNCTIONS ######################



    
    def get_output_folder_path(self):
        return self.root_path + 'Breakdowns' + os.sep
    
        
    def pickle_dump(self):
        ## If the output 'folder' doesn't exist, create it!
        if not (os.path.exists(self.get_output_folder_path())):
            os.makedirs(self.get_output_folder_path())
        
        pickle_out = open(self.file_path, "wb")
        pickle.dump(self.metadata, pickle_out)
        
    
    def pickle_read(self, file_path=''):
        
        if file_path == '':                 # IF a path isn't explicitly specified, then use the internal filepath.
            file_path = self.file_path    
            
        pickle_in = open(file_path, "rb")
        self.metadata = pickle.load(pickle_in)