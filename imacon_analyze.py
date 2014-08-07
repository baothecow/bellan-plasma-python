# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 21:23:01 2014

@author: bao

There are various functions to aid with image analysis.

rebin           -- can be used to resize a image by integer multiples.
get_imacon_data -- 
"""

import numpy as np
import PIL.Image as Image
import Tkinter, tkFileDialog
import struct
from file_io_lib import pickle_read
from parameters import exp_paths
import os
import idl_support as idlsup


INITIAL_DIR = 'E:\\data\\singleloop\\singleloop_imacon\\fast_view'
#INITIAL_DIR = 'D:\\Dropbox\\Research Summaries Files\\201401\\he_h_imacon_variation\\1009_1010_1111'
OUTPUT_DIR = ''


## Implementing IDL's rebin in Python
## http://stackoverflow.com/questions/8090229/resize-with-averaging-or-rebin-a-numpy-2d-array
## Will return the results as an integer.
def rebin(a, shape):
    sh = shape[0],a.shape[0]//shape[0],shape[1],a.shape[1]//shape[1]
    return  a.reshape(sh).mean(-1).mean(1).astype(int)
    

## Routine to read an image and return the appropriate array of values.
## User can choose the resize_factor to rescale the image.
def get_imacon_data(path, resize_factor=2, verbose=True):
    ## Open the image and get data
    image = Image.open(path)
    if verbose:
        print "Reading from " + path
    return resize_imacon_image(image, resize_factor=resize_factor, verbose=verbose)

    
def resize_imacon_image(image, resize_factor=2):
    """ Routine which reads and resizes an imacon image """
    # The [::-1] reverses the "size" list eg. (3920,4800) instead of (4800,3920)
    image_shape = image.size[::-1]
    im = np.array(image.getdata())
    ## By default the array option gives a 1D array.  Converts back to 2d array.
    im = np.reshape(im, image_shape)
    ## Use shape() to get shape of image and then use rebin to resize it.
    resized_img = rebin(im, np.divide(image_shape, resize_factor).tolist())
    return resized_img
    
    
def get_file_paths(folderpath=INITIAL_DIR):
    """ Asks the user to choose some files and returns a list of paths for those files """
    ## Scripts to ask the user for choose the file to be read.
    ## Inspired by: http://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
    ## and http://stackoverflow.com/questions/4116249/parsing-the-results-of-askopenfilenames
    root = Tkinter.Tk()
    root.withdraw()
    file_path = tkFileDialog.askopenfilenames(initialdir=folderpath)
    
    # Splits the results into a list of files.
    return root.tk.splitlist(file_path)
    
def imacon_choose_frame(imagepath, frame_num):
    """ Takes in an imacon image of 16 frames and returns the chosen frame as an image """
    
    imarr = get_imacon_data(imagepath, resize_factor=1)
    image_shape = np.shape(imarr)

    
    frame_x_size = image_shape[0]/4
    frame_y_size = image_shape[1]/4
    
    x_position = (frame_num - 1) // 4
    y_position = (frame_num - 1) % 4
    
    
    return Image.fromarray(imarr[(x_position) * frame_x_size:(x_position+1) * frame_x_size, 
                              y_position * frame_y_size:(y_position + 1) * frame_y_size])
    

def imacon_generate_new_output_path(imagepath, extra='_extra'):
    """ Adds extra str just before the extension.  eg.  'a.txt' --> 'a_extra.txt' """
    
    patharr = imagepath.split('.')
    prefix = ".".join(patharr[0:-1])  # Extract everything except the extension.
    return "".join(prefix + extra + '.' + patharr[-1])


def make_image_list_from_large_image(large_image, subdivision=(4, 4), frames=(1, 14), resize_factor=2):
    img_list = list()    
    
    resized_image = resize_imacon_image(large_image, resize_factor=resize_factor)
    list_img_arr = make_image_list_from_large_image_array(resized_image, subdivision=subdivision, frames=frames)
    
    for img_arr in list_img_arr:
        img_list.append(Image.fromarray(img_arr))
    return img_list
        


def make_image_list_from_large_image_array(img_arr, subdivision=(4, 4), frames=(1, 14)):
    """ Takes in a numpy array that is representative of a picture containing
    embedded pictures of the same size and recreates it as a 3d array.
    
    Format of subdivision is in (factor to divide the width, factor to divide the height)
    
    Returns a lists of numpy arrays whose elements are the frames within the image.
    """
    
    list_img_arr = list()    
    
    (height, width) = np.shape(img_arr)
    
    sub_im_height = height/subdivision[1]
    sub_im_width = width/subdivision[0]
    
    # Note.  The array starts from the upper right hand corner of png images.
    for frame in range(frames[0]-1, frames[1]):
        #print (frame // 4) % 4, frame % 4
        list_img_arr.append(img_arr[sub_im_height*((frame // 4) % 4): sub_im_height*((frame // 4) % 4 + 1),  \
                               sub_im_width*(frame % 4): sub_im_width*(frame % 4 + 1)])
                       
    
    
    return list_img_arr
    
def check_existence_of_timing_file(shotnum):
    folderpath = exp_paths['singleloop.METADATA']+'imacon_timing\\'
    path = folderpath + 'meta_solimc' + "%05d" % shotnum + '.pickle'
    return os.path.exists(path)
    
def get_imacon_timing_from_pickled_shot(shotnum):
    """ Return the imacon timing for a specific shot.
    Input: a shotnumber.
    Returns: a tuple whose first element is an array of shot times and whose
    second element is a list of exposure times.
    """
    folderpath = exp_paths['singleloop.METADATA']+'imacon_timing\\'
    path = folderpath + 'meta_solimc' + "%05d" % shotnum + '.pickle'
    return pickle_read(path)
    
def get_reduced_imacon_path(shotnum):
    """ Returns the path to the reduced imacon file """
    
    root = exp_paths['singleloop.REDUCED_PATH']

    # Get date from the pickle file if it exists.
    date_pickle_path = exp_paths['singleloop.METADATA']+'date\\'+str(shotnum)+'_date.pickle'
    #print date_pickle_path
    if os.path.exists(date_pickle_path):
        date = pickle_read(date_pickle_path)
    else:  # Run foldername.pro to obtain the date.
        date = idlsup.get_shot_date(shotnum)    
        
    constructor = '\\Reduced_solimc' + "%05d" % shotnum + '.png'

    return root + date + constructor

def get_shotnum_from_path(path):
    """ This program takes a path, extracts the basename, removes the extension, and then takes the last 5 characters and
    converts that to a number """
    filebasename = os.path.basename(path)
    filename = os.path.splitext(filebasename)[0]
    shotnum = filename[-5:]
    try:
        shotnum = int(shotnum)
    except:
        print 'Oops!  get_shotnum_from_path in imacon_analyze expected the last 5 digits of the filename to be the shotnum.  Setting to 1000'
        shotnum = 1000

    return shotnum
    
    
###Magnus' port of Bao's idl code: extract_imacon_times_from_footer.pro
def imacon_times(path, TIME_CONVERSION=1e3):

    def lindgen(n):
        return np.arange(0,n)
    #-------------------- User Adjustable  constants ---------------------------------------
    #TIME_CONVERSION = 1e3		    # Set at 1 for ns, 1e3 for microsecond, 1e6 for ms.
    #---------------------------------------------------------------------------------------

    #-------------------- Relevant  constants ----------------------------------------------

    BYTE_FOOTER_PACKET_SIZE = 11016	    # Number of bytes / info packet in footer for each CCD.
    BYTE_CCD1_START_TIME = 37651208	    # Byte location of Start time of first frame in ns.
    BYTE_CCD1_EXPOSURE_1 = 37651344
    BYTE_CCD1_EXPOSURE_2 = 37651352
    BYTE_CCD1_DELAY = 37651600
    FRAMES = 14			    # Number of working imacon frames (ie # working CCDs * 2)

    #---------------------------------------------------------------------------------------

    # Create appropriate arrays.
    byte_start_time_1_array = BYTE_CCD1_START_TIME + BYTE_FOOTER_PACKET_SIZE*lindgen(FRAMES/2)
    byte_exposure_1_array   = BYTE_CCD1_EXPOSURE_1 + BYTE_FOOTER_PACKET_SIZE*lindgen(FRAMES/2)
    byte_exposure_2_array   = BYTE_CCD1_EXPOSURE_2 + BYTE_FOOTER_PACKET_SIZE*lindgen(FRAMES/2)
    byte_delay_array        = BYTE_CCD1_DELAY      + BYTE_FOOTER_PACKET_SIZE*lindgen(FRAMES/2)


    # Read in the data associated with the tiff.
    fin=open(path,"rb")
    tiffdata= fin.read()

    # Note that imacon tiffs are set in a little-endian style.  Read up about that to understand the following commands.
    # ** I am accessing the data array at the index location denoted by the byte_start_time_array.
    # ** Know that the format is a long thus will need to read in 4 bytes to get the true value.

    start = np.zeros(FRAMES)
    exp1   = np.zeros(FRAMES/2)
    exp2   = np.zeros(FRAMES/2)
    delay  = np.zeros(FRAMES/2)

    for pos in range(0,FRAMES/2):
        i1 = byte_start_time_1_array[pos]
        i2 = byte_exposure_1_array[pos]
        i3 = byte_exposure_2_array[pos]
        i4 = byte_delay_array[pos]

        val = struct.unpack("<L", tiffdata[i1:i1 +4])[0]/TIME_CONVERSION
        start[pos] = val

        val2 = struct.unpack("<L", tiffdata[i2:i2 +4])[0]/TIME_CONVERSION
        exp1[pos] = val2

        val3 = struct.unpack("<L", tiffdata[i3:i3 +4])[0]/TIME_CONVERSION
        exp2[pos] = val3

        val4 = struct.unpack("<L", tiffdata[i4:i4 +4])[0]/TIME_CONVERSION
        delay[pos] = val4

    start[FRAMES/2:] = start[0:FRAMES/2] + exp1 + delay

    return start,np.append(exp1,exp2)