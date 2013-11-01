## Testing magnus's IO library.

from vme_plot import *
from vme_plot_specific import * 
import numpy as np
import matplotlib.pyplot as plt
from vme_analyze import *
from cookb_signalsmooth import smooth


shotnums = ['843', ['844', '845'], '846']


#vme_plot_current(shotnums)

vme_plot_diag_for_shots(shotnums, diag='current')
#
#
#
##
#data = vme_avg_sig(shotnums, diag='current')
#
#plt.plot(data[0], smooth(data[1], 50), '-k', linewidth=2)
#
##vme_plot_diagnostic(data[0], smooth(data[1], 50), diag='tek_hv')

#shotnums=['843', '844', '845', '846']
#data = vme_avg_sig(shotnums, diag='tek_hv')
#data2 = vme_avg_sig(shotnums, diag='current')
#vme_2diag_2d_plot(data[0], smooth(data[1], 50), smooth(data2[1], 50))


#Checking to see if object is string

#foo = ['hi']
#bar = 'hi'
#
#if isinstance(foo, basestring): print 'hi'