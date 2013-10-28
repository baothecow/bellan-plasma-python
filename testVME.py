## Testing agnus's IO library.

from file_io_lib import readVME
from vme_plot import vme_plot_current
import numpy as np


root = 'D:\\data\\singleloop_VME\\data\\'
root = 'G:\\data\\singleloop\\singleloop_VME\\data\\'

foldername = '2013.03.14\\'

shotnum = '562'

title = 'This is my plot'

constructor = 'vi_t2ch13_' + shotnum + '.dat'
rows=3


filename = root + foldername + constructor

data = readVME(filename, rows=rows)

vme_plot_current(data, title=title)





