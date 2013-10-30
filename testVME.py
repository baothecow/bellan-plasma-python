## Testing magnus's IO library.

from file_io_lib import readVME
from vme_plot import *
from vme_plot_specific import vme_plot_current
import numpy as np
import matplotlib.pyplot as plt


##shotnum = ['570', '571', '572']
##
##vme_plot_current(shotnum)



root = 'D:\\data\\singleloop_VME\\data\\'
root = 'G:\\data\\singleloop\\singleloop_VME\\data\\'

foldername = '2013.03.14\\'

shotnum = ['570', '571', '572']

title =  'This is my plot'
ytitle = 'Current (kA)'
rows=3


plt.figure(1)
for counter in range(0, len(shotnum)):
    constructor = 'vi_t2ch13_' + shotnum[counter] + '.dat'
    filename = root + foldername + constructor
    data = readVME(filename, rows=rows)
    vme_basic_2d_plot_from_dict(data[0, :], data[2, :])


plt.figtext(.5,.85,'Shot(s): ' + ", ".join(shotnum), fontsize=10,ha='center')
plt.show()
##
##ylim1=(-5e3, 5e3)
##
##plt.figure(2)
##for counter in range(0, len(shotnum)):
##    constructor = 'vi_t2ch13_' + shotnum[counter] + '.dat'
##    filename = root + foldername + constructor
##    data = readVME(filename, rows=rows)
##    vme_2params_2d_plot(
##        data[0, :],
##        data[1, :],
##        data[2, :],
##        ylim1=ylim1,
##        color_counter=counter)
##
##
##plt.figtext(.5,.85,'Shot(s): ' + ", ".join(shotnum), fontsize=10,ha='center')
##plt.show()
