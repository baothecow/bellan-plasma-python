## Testing agnus's IO library.

from file_io_lib import readVME
from vme_plot import vme_basic_2d_plot
from vme_plot import vme_2params_2d_plot
import numpy as np
import matplotlib.pyplot as plt


root = 'D:\\data\\singleloop_VME\\data\\'
root = 'G:\\data\\singleloop\\singleloop_VME\\data\\'

foldername = '2013.03.14\\'

shotnum = ['570', '571', '572']

title =  'This is my plot'
ytitle = 'Current (kA)'
rows=3


##plt.figure(1)
##for counter in range(0, len(shotnum)):
##    constructor = 'vi_t2ch13_' + shotnum[counter] + '.dat'
##    filename = root + foldername + constructor
##    data = readVME(filename, rows=rows)
##    vme_basic_2d_plot(data[0, :], data[2, :], style_counter=counter, ytitle=ytitle)
##
##
##plt.figtext(.5,.85,'Shot(s): ' + ", ".join(shotnum), fontsize=10,ha='center')
##plt.show()


ylim1=(-5e3, 5e3)

plt.figure(2)
for counter in range(0, len(shotnum)):
    constructor = 'vi_t2ch13_' + shotnum[counter] + '.dat'
    filename = root + foldername + constructor
    data = readVME(filename, rows=rows)
    vme_2params_2d_plot(
        data[0, :],
        data[1, :],
        data[2, :],
        ylim1=ylim1,
        style_counter=counter)


plt.figtext(.5,.85,'Shot(s): ' + ", ".join(shotnum), fontsize=10,ha='center')
plt.show()
