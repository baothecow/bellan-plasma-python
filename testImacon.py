# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 23:20:57 2014

@author: bao
"""

### Script files for running imacon.


# Script to make movie from reduced imacon file.
from imacon_analyze import make_movie_from_reduced_png






### Scripts for extracting a specific frame from a list of imacon images.
#from imacon_analyze import imacon_choose_frame, get_file_paths, imacon_generate_new_output_path, INITIAL_DIR
#
#framenum = 4
#filepaths = get_file_paths(folderpath=INITIAL_DIR)
#
#for path in filepaths:
#    im = imacon_choose_frame(path, framenum)
#    im.convert('RGB').save(imacon_generate_new_output_path(path, extra='_frame' + str(framenum)))
