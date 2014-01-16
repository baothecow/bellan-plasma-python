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

#INITIAL_DIR = 'E:\\data\\singleloop\\singleloop_imacon\\fast_view'
INITIAL_DIR = 'D:\\Dropbox\\Research Summaries Files\\201401\\he_h_imacon_variation\\1009_1010_1111'
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
    # The [::-1] reverses the "size" list eg. (3920,4800) instead of (4800,3920)
    image_shape = image.size[::-1]
    if verbose:
        print "Reading from " + path
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



