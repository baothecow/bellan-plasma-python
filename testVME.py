## Testing agnus's IO library.

from file_io_lib import readVME
from vme_plot import vme_plot_current
import numpy as np


root = 'D:\\data\\singleloop_VME\\data\\'
root = 'G:\\data\\singleloop\\singleloop_VME\\data\\'

foldername = '2013.03.14\\'

shotnum = '562'

title = 'This is my plot'


filename = root + foldername + 'HV_'+ shotnum + '.dat'

data = readVME(filename)

vme_plot_current(data, title=title)





