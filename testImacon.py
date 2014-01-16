# -*- coding: utf-8 -*-
"""
Created on Mon Jan 06 23:20:57 2014

@author: bao
"""

### Script files for running imacon.

from imacon_analyze import *



framenum = 8
filepaths = get_file_paths(folderpath=INITIAL_DIR)

for path in filepaths:
    im = imacon_choose_frame(path, framenum)
    im.convert('RGB').save(imacon_generate_new_output_path(path, extra='_frame' + str(framenum)))
