# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 23:20:57 2014

@author: bao
"""

### Script files for running imacon.


# Script to make movie from reduced imacon file.
from imacon_analyze import make_image_list_from_large_image_array, get_imacon_data, imacon_times
from parameters import exp_paths

## PNG images are 16 bit.
lb_dynamic_range = 0
ub_dynamic_range = 2**16-1

reduced_path = exp_paths['singleloop.REDUCED_PATH']
path = reduced_path + '2014.07.10\\Reduced_solimc02058.png'

#path = exp_paths['singleloop.IMACON_PATH'] + '2014.07.10\\solimc02058.TIF'


#print imacon_times(path)

img_arr = get_imacon_data(path, resize_factor=2)

movie = make_image_list_from_large_image_array(img_arr)


plt.imshow(movie[5], cmap="hot", vmin=lb_dynamic_range, vmax=ub_dynamic_range)











### Scripts for extracting a specific frame from a list of imacon images.
#from imacon_analyze import imacon_choose_frame, get_file_paths, imacon_generate_new_output_path, INITIAL_DIR
#
#framenum = 4
#filepaths = get_file_paths(folderpath=INITIAL_DIR)
#
#for path in filepaths:
#    im = imacon_choose_frame(path, framenum)
#    im.convert('RGB').save(imacon_generate_new_output_path(path, extra='_frame' + str(framenum)))
