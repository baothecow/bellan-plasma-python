""" Contains functions which allow python-idl interactivity 


    Example: get_shot_date(shotnum) returns a string with date.



"""

import subprocess
import os

ENVIR = {'PATH': 'C:\\Program Files\\ITT\\IDL\\IDL81\\bin\\bin.x86_64\\'}
PY_LIB_PATH = 'C:\\Users\\Bao\\Documents\\GitHub\\bellan-plasma-python\\'
IDL_LIB_PATH = 'G:\\programs\\idl\\singleloop_lib\\'
IDL_VME_PATH = 'G:\\data\\singleloop\\singleloop_VME\\data\\'


def gen_read_foldername_pro(shotnum):
    """ Gen temp file to call IDL's foldername
    
        shotnum - integer corresponding to a shot number.
    
    """
    
    f = open(PY_LIB_PATH + 'temp_idl_file.pro','w')
    f.write(".compile " + IDL_LIB_PATH + "foldername.pro\n")
    f.write("folder = \"\"\n")
    f.write("foldername, " + str(shotnum) + ", folder, verbal=1\n")
    f.write("wait, 0.01\n")       # Process may terminate too early otherwise.
    f.close()


def get_idl_lib_path():
    """ Returns the path to the main IDL library """
    return IDL_LIB_PATH

def get_idl_vme_path():
    """ Returns the path to the VME data """
    return IDL_VME_PATH
    
    
def run_temp_idl_file_pro():
    """ Use subprocess to run temp_idl_file.pro if one exists """
    
    subp = subprocess.Popen("idl -e \"@" + PY_LIB_PATH + "temp_idl_file.pro\"",
        stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell = True, 
        env=ENVIR)
    
    # Extracts the output.
    (idl_stdout, idl_stderr) = subp.communicate()

    # Split the string into individual lines and print the last line.
    stringarr = idl_stdout.split()
    # The last string should be the date desired.
    return stringarr[-1]
    
def get_shot_date(shotnum):
    """ Returns the date associated with a shot by using foldername.pro """

    # If shotnum is a string, convert it to an integer.
    shotnum = int(shotnum)
    
    # Generates a temp .pro to read foldername and extract the shot date.
    gen_read_foldername_pro(shotnum)        
    date = run_temp_idl_file_pro()
    os.remove(PY_LIB_PATH + "temp_idl_file.pro")
    return date
    
