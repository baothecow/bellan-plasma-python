# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 14:09:34 2014

@author: bao
"""

import os as os
import cPickle as pickle


## Creating an object which contains breakdown time.
class DictOfBreakdowns:
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
        self.file_path = self.root_path + 'Breakdowns' + os.sep + 'BreakdownDict.pickle'
    
    def check_existence_pickle_file(self):
        return os.path.exists(self.file_path)

    def initialize_obj(self):
        """ Create an empty dict by default.  Populate the dict if a pickle file exists. """
        self.breakdowns = dict()
        if self.check_existence_pickle_file():
            self.pickle_read()
            
    ### INTERACTIVE FUNCTIONS
        
    def get_breakdown_time(self, shotnum):
        return self.breakdowns[str(shotnum)][0]
        
    def set_breakdown_time(self, shotnum, time):
        self.breakdowns[str(shotnum)] = (time, self.get_date(shotnum))
        
    def get_breakdown_time_date(self, shotnum):
        return self.breakdowns[str(shotnum)]
        
        
    def print_all_keys(self):
        for key in self.breakdowns:
            print (key, self.breakdowns[key])
            print '--------'

    
    ######### IO FUNCTIONS ######################
    
    def get_output_folder_path(self):
        return self.root_path + 'Breakdowns' + os.sep
    
    def get_date(self, shotnum):
        """ 
        Check for existence of date file.
        """
        date_path = self.root_path + 'date' + os.sep + str(shotnum) + '_date.pickle'
        if os.path.exists(date_path):
            return pickle.load(open(date_path, "rb"))
        else:
            return 'No metadate'
        
    def pickle_dump(self):
        ## If the director 'folder' doesn't exist, create it!
        if not (os.path.exists(self.get_output_folder_path())):
            os.makedirs(self.get_output_folder_path())
        
        pickle_out = open(self.file_path, "wb")
        pickle.dump(self.breakdowns, pickle_out)
        
    
    def pickle_read(self, file_path=''):
        
        if file_path == '':                 # IF a path isn't explicitly specified, then use the internal filepath.
            file_path = self.file_path    
            
        pickle_in = open(file_path, "rb")
        self.breakdowns = pickle.load(pickle_in)