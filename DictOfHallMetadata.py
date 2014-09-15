# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 14:09:34 2014

@author: bao
"""

import os as os
import cPickle as pickle


## Creating an object which contains breakdown time.
class DictOfHallMetadata:
    """
    Class is a dict which stores the breakdown times.
    
    Stores a dict of (breakdown_time, shotdate)
    
    
    """
    
    def __init__(self, root_path):
        self.root_path = root_path
        self.update_file_path()
        self.initialize_obj()
        
    ### INITIALIZATION FUNCTIONS ###
    
    def update_file_path(self):
        self.file_path = self.root_path + 'metadata' + os.sep + str(self.descript) + '_' + self.get_shot_summary_string() + '.pickle'

    def get_shot_summary_string(shotnums):
        """ 
        Used to generate a summary string given a list of integer shotnumbers.   
        
        >>> shotnums = range(100, 123)
        >>> get_shot_summary_string(shotnums)
        '100_101_102_19_shots_122'
        
        >>> shotnums = [123, 111, 165]
        >>> get_shot_summary_string(shotnums)
        '123_111_165'
        
        """
    
        numElements = len(shotnums)
        num_pre_shots = 3
        summary_string = ""
        
        if numElements <= num_pre_shots + 1:
            for i in range(0, numElements - 1):
                summary_string = summary_string + str(shotnums[i]) + "_"
        else:
            for i in range(0, num_pre_shots):
                summary_string = summary_string + str(shotnums[i]) + "_"
            summary_string = summary_string  + str(numElements - num_pre_shots - 1) + '_shots_'
                
        summary_string = summary_string + str(shotnums[numElements - 1])
        return summary_string

    
    def check_existence_pickle_file(self):
        return os.path.exists(self.file_path)

    def initialize_obj(self):
        """ Create an empty dict by default.  Populate the dict if a pickle file exists. """
        self.metadata = dict()
        if self.check_existence_pickle_file():
            self.pickle_read()
            
    ### INTERACTIVE FUNCTIONS
        
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

def get_shot_summary_string(shotnums):
    """ 
    Used to generate a summary string given a list of integer shotnumbers.   
    
    >>> shotnums = range(100, 123)
    >>> get_shot_summary_string(shotnums)
    '100_101_102_19_shots_122'
    
    >>> shotnums = [123, 111, 165]
    >>> get_shot_summary_string(shotnums)
    '123_111_165'
    
    """

    numElements = len(shotnums)
    num_pre_shots = 3
    summary_string = ""
    
    if numElements <= num_pre_shots + 1:
        for i in range(0, numElements - 1):
            summary_string = summary_string + str(shotnums[i]) + "_"
    else:
        for i in range(0, num_pre_shots):
            summary_string = summary_string + str(shotnums[i]) + "_"
        summary_string = summary_string  + str(numElements - num_pre_shots - 1) + '_shots_'
            
    summary_string = summary_string + str(shotnums[numElements - 1])
    return summary_string

    
    def get_output_folder_path(self):
        return self.root_path + 'Breakdowns' + os.sep
    
        
    def pickle_dump(self):
        ## If the director 'folder' doesn't exist, create it!
        if not (os.path.exists(self.get_output_folder_path())):
            os.makedirs(self.get_output_folder_path())
        
        pickle_out = open(self.file_path, "wb")
        pickle.dump(self.metadata, pickle_out)
        
    
    def pickle_read(self, file_path=''):
        
        if file_path == '':                 # IF a path isn't explicitly specified, then use the internal filepath.
            file_path = self.file_path    
            
        pickle_in = open(file_path, "rb")
        self.metadata = pickle.load(pickle_in)