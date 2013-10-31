""" Contains functions which allow python-idl interactivity 


    Example: get_shot_date(shotnum) returns a string with date.



"""

import subprocess
import os

ENVIR = {'PATH': 'C:\\Program Files\\ITT\\IDL\\IDL81\\bin\\bin.x86_64\\'}
PY_LIB_PATH = 'C:\\Users\\Bao\\Documents\\GitHub\\bellan-plasma-python\\'
IDL_LIB_PATH = 'G:\\programs\\idl\\singleloop_lib\\'


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
    """ Returns the IDL_LIB_PATH variable """
    return IDL_LIB_PATH
    
    
def run_temp_idl_file_pro():
    """ Use subprocess to run temp_idl_file.pro if one exists """
    
    subp = subprocess.Popen("idl -e \"@" + PY_LIB_PATH + "temp_idl_file.pro\"",
        stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell = True, 
        env=ENVIR)
    
    # Extracts the output.
    (idl_stdout, idl_stderr) = subp.communicate()

    # Split the string into individual lines and print the last line.
    stringarr = idl_stdout.split()
    print stringarr[-1]
    
    
def get_shot_date(shotnum):
    """ Returns the date associated with a shot by using foldername.pro """
    
    # Generates a temp .pro to read foldername and extract the shot date.
    gen_read_foldername_pro(shotnum)        
    run_temp_idl_file_pro()
    os.remove(PY_LIB_PATH + "temp_idl_file.pro")
    

get_shot_date(500)
    

#
## Remove the temporary file
#
#
#
##print(idl_stdout)   # for python 2.4, use "print idl_stdout" instead
#
## Make a copy.  Manipulating this output directly messes things up for
## some mysterious reason.
#idl_output = idl_stdout
#
## Split the string into individual lines.
#stringarr = idl_output.split()
#print stringarr[-1]
#
#
