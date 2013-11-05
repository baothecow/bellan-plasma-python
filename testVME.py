## Testing magnus's IO library.

from vme_plot import *
from vme_plot_specific import * 
import numpy as np
import matplotlib.pyplot as plt
from vme_analyze import *
from cookb_signalsmooth import smooth

from vme_analyze import integrate




#

#shotnums = [['843', '844', '845', '846'], ['847', '848', '849'], \
#            ['851', '852', '853', '854', '855'], \
#            ['856', '857', '858'], ['859', '860', '861', '862', '863'], \
#            ['864', '865', '866', '867', '868']]
#
#descript = ['0V', '15V', '30V', '45V','60V', '75V', '90V']
#
#vme_plot_diag_for_shots(shotnums, diag='sol_mpa')




mpa_data = vme_avg_sig(['848', '849'], diag='sol_mpa')

time = mpa_data['time']
bdot = (mpa_data['bx'], mpa_data['by'], mpa_data['bz'])
b = get_b_from_bdot(time, bdot)

vme_plot_diagnostic(time, b, diag='sol_mpa.int')





#
#
#plt.figure()
#dt = time[1] - time[0]
#plt.subplot(211)
#plt.plot(time, integrate(dt, vector[0]))
#plt.xlim(15,30)
#plt.subplot(212)
#plt.plot(time, vector[0])
#plt.xlim(15,30)





#data = vme_avg_sig(['847', '848', '849', '850'], diag='tek_hv')
#
#time = data[0]
#signal = data[1]
#
#bottom_ind = 1450
#top_ind = 3000
#
#plt.plot(time[bottom_ind:top_ind], signal[bottom_ind:top_ind])

#vme_plot_diagnostic(time, vector, diag='sol_mpa')

#shotnums = [['847', '873', '874', '875']]
#vme_plot_diag_for_shots(shotnums, diag='iso_hv', descript=descript)


#shotnums = [map(str, range(241, 247)), map(str, range(247, 250)), \
#            ['250', '252', '253'], ['254', '255', '256'], \
#            ['257', '258', '259', '260']]
#
#descript = ['0V', '50V', '100V', '150V', '200V']
#
#vme_plot_diag_for_shots(shotnums, diag='current', descript=descript)





#shotnums = [['879', '880', '881'], ['882', '883', '884'], \
#            ['885', '886', '887'], ['888', '889', '890']]
#            
#descript = ['0V', '30V', '60V', '90V']
#
#
##shotnums = ['843', '844', '845', '846']
##shotnums = ['847', '848', '849']
##shotnums = ['851', '852', '853', '854', '855']
##shotnums = ['856', '857', '858']
##shotnums = ['859', '860', '861', '862', '863']
##shotnums = ['864', '865', '866', '867', '868']
#
##shotnums = ['850', '851', '852', '853', '854', '855', ['850', '851', '852', '853', '854', '855']]
#
##vme_plot_current(shotnums)
#
#vme_plot_diag_for_shots(shotnums, diag='current', descript=descript)
#
#
#
##
#data = vme_avg_sig(shotnums, diag='current')
#
#plt.plot(data[0], smooth(data[1], 50), '-k', linewidth=2)

#vme_plot_diagnostic(data[0], smooth(data[1], 50), diag='tek_hv')

#shotnums=['843', '844', '845', '846']
#data = vme_avg_sig(shotnums, diag='tek_hv')
#data2 = vme_avg_sig(shotnums, diag='current')
#vme_2diag_2d_plot(data[0], smooth(data[1], 50), smooth(data2[1], 50))


#Checking to see if object is string

#foo = ['hi']
#bar = 'hi'
#
#if isinstance(foo, basestring): print 'hi'
#if isinstance(foo, list): print 'bye'
#if isinstance(bar, basestring): print 'hi2'
#if isinstance(bar, list): print 'bye2'
