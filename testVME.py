## Testing magnus's IO library.

from vme_plot import *
from vme_plot_specific import * 
from vme_cust_plot import *
import numpy as np
import matplotlib.pyplot as plt
from vme_analyze import *
from cookb_signalsmooth import smooth
from parameters import exp_paths, plot_diag_params
from vme_analyze import integrate



diag = 'current'
#shotnums = [['1160', '1161', '1163'], ['1164', '1165', '1166'], ['1167', '1168', '1169'], \
#            ['1170', '1172'], ['1173', '1174', '1175'], ['1176', '1177', '1178'], \
#            ['1179', '1180'], ['1182', '1183'], ['1185', '1186', '1187'], \
#            ['1188', '1189', '1190'], ['1191', '1192', '1193']]



strarr1 = map(str, [1160, 1161, 1162])
strarr2 = map(str, [1176, 1177, 1178])
strarr3 = map(str, [1170, 1171, 1172])

# Convoluted method to change ['1', '2', '3'] to [['1'], ['2'], ['3']]

shots1 = vme_unflatten_list(strarr1)
shots2 = vme_unflatten_list(strarr2)
shots3 = vme_unflatten_list(strarr3)

(peak_times, peak_values) = vme_get_shot_peak_time_and_value(shots1, diag)
plt.scatter(peak_times, peak_values, c='g')
(peak_times, peak_values) = vme_get_shot_peak_time_and_value(shots2, diag)
plt.scatter(peak_times, peak_values, c='b')
(peak_times, peak_values) = vme_get_shot_peak_time_and_value(shots3, diag)
plt.scatter(peak_times, peak_values, c='r')
plt.show()






#diag = 'current'
#shotnums = [['1160', '1161', '1163'], ['1164', '1165', '1166'], ['1167', '1168', '1169'], \
#            ['1170', '1172'], ['1173', '1174', '1175'], ['1176', '1177', '1178'], \
#            ['1179', '1180'], ['1182', '1183'], ['1185', '1186', '1187'], \
#            ['1188', '1189', '1190'], ['1191', '1192', '1193']]
#descript = ['0V', '-30V', '-60V', '-90V', '-120V', '-150V', '30V', '60V', '90V', '120V', '150V']
#vme_plot_diag_for_shots(shotnums, diag, descript)
##plot_diag_params['sol_mpa.int.xlim'] = [15, 25]
##plot_diff_mpa_for_shots(shotnums, descript=descript, num_probe=1)




#diag = 'sol_mpa'
#shotnums = [['1159'], ['1157'], ['1154'], ['1151'], ['1145'], ['1148']]
#descript = ['0V', '30V', '60V', '90V', '120V', '150V']
##vme_plot_diag_for_shots(shotnums, diag, descript)
#plot_diag_params['sol_mpa.int.xlim'] = [15, 25]
#plot_diff_mpa_for_shots(shotnums, descript=descript, num_probe=1)


#
##diag = 'sol_mpa'
#exp_paths['EXP'] = 'hall'
#shotnums = [['226'], ['227']]
#plot_hall_for_shots(shotnums)
##descript = ['0G', '15V', '30V', '45V', '60V', '75V', '90V']
##plot_diff_mpa_for_shots(shotnums,descript=descript, num_probe=1)
##plot_sol_mpa_for_shots(shotnums, num_probe=4)
##vme_plot_diag_for_shots(shotnums, diag) #, descript)

#diag = 'sol_mpa'
#shotnums = [['954', '955', '956'], ['975', '976', '977'], ['957', '958', '959'], \
#            ['972', '973', '974'], ['960', '961', '962'], ['969', '970', '971'], \
#            ['963', '964', '965']]
#descript = ['0G', '15V', '30V', '45V', '60V', '75V', '90V']
#plot_diff_mpa_for_shots(shotnums,descript=descript, num_probe=1)
##plot_sol_mpa_for_shots(shotnums, descript=descript, num_probe=1)
##vme_plot_diag_for_shots(shotnums, diag, descript)



#diag = 'current'
#shotnums = [['1002', '1003', '1004'], ['1005', '1006', '1007'], ['1008', '1009', '1010'], \
#['1011', '1012', '1013'], ['1014', '1015', '1016']]
#descript = ['3kV', '3.5kV', '4kV', '4.5kV', '5kV']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript)




#diag = 'sol_mpa'
#shotnums = [['844', '845', '846'], \
#['851', '854', '855'], \
#['860', '861', '863'], \
#['870', '871', '872']]
#descript = ['0V', '30V', '60V', '90V']
#plot_diff_mpa_for_shots(shotnums,descript=descript)



#diag = 'sol_mpa'
#shotnums = [['954', '955', '956'], ['975', '976', '977'], ['957', '958', '959'], \
#            ['972', '973', '974'], ['960', '961', '962'], ['969', '970', '971'], \
#            ['963', '964', '965']]
#descript = ['0G', '15V', '30V', '45V', '60V', '75V', '90V']
#plot_diff_mpa_for_shots(shotnums,descript=descript)
##vme_plot_diag_for_shots(shotnums, diag, descript)

#diag = 'current'
#shotnums = ['10382', '10385', '10387', '10389', '10391', ['10382', '10385', '10387', '10389', '10391']]
#descript = ['0G', '150G', '300G', '450G', '600G']
#delay = vme_get_breakdown_times(shotnums)
#delay = np.multiply(delay, -1)
#vme_plot_diag_for_shots(shotnums, diag, descript, delay)



#shot = '10538'
#data = vme_get_breakdown_time(shot)
#time = list(data[0][500:])
#signal = data[1][500:]
#diff = list(np.diff(signal))
#
#
#diff.index(max(diff))
#
#
#plt.plot(time, diff)
#plt.plot(time, signal)


#diag = 'tek_hv'
#shotnums = ['10382', '10385', '10387', '10389', '10391']
#descript = ['0G', '150G', '300G', '450G', '600G']
##delay = [-14.46, -14.46]
#vme_plot_diag_for_shots(shotnums, diag, descript)#, delay)



#diag = 'tek_hv'
#shotnums = [['834', '835', '836'], ['828', '829', '830'], ['822', '823', '824'], \
#['879', '880', '881', '904', '905', '906', '907', '843', '844', '845', '846'], \
#    ['899', '900', '901', '902', '903', '851', '854', '855'], \
#    ['885', '886', '887', '895', '896', '897', '860', '861', '863'], \
#    ['888', '889', '890', '891', '892', '893', '894', '869', '870', '871', '872']]
#descript = ['-90V', '-60V', '-30V', '0V', '30V', '60V', '90V']
#delay = [-.67, -.67, -.67, 0, 0, 0, 0]
#vme_plot_diag_for_shots(shotnums, diag, descript, delay)



## Plots the antistrapping currents for 0, 30, 60, 90 for the poster.
#diag = 'tek_hv'
#shotnums = [['879', '880', '881', '904', '905', '906', '907', '843', '844', '845', '846'], \
#    ['882', '883', '884', '899', '900', '901', '902', '903', '851', '854', '855'], \
#    ['885', '886', '887', '895', '896', '897', '860', '861', '863'], \
#    ['888', '889', '890', '891', '892', '893', '894', '869', '870', '871', '872']]
#descript = ['0V', '30V', '60V', '90V']
#vme_plot_diag_for_shots(shotnums, diag, descript)



## Plots the antistrapping currents for 0, 30, 60, 90 for the poster.
#diag = 'tek_hv'
#shotnums = [['815', '816', '817', '818'], ['822', '823', '824'], \
#        ['828', '829', '830'], ['834', '835', '836']]
#descript = ['0V', '30V', '60V', '90V']
#vme_plot_diag_for_shots(shotnums, diag, descript)



## Compare 0V for no strap vs 0V for strap configuration.
#diag = 'current'
#shotnums = [['815', '816', '817', '818'], ['879', '880', '881', '904', '905', '906', '907', '843', '844', '845', '846']]
#descript= ['0V - Anti-strap', '0V - Strap']
#vme_plot_diag_for_shots(shotnums, diag, descript)



# Plots the antistrapping currents.
#diag = 'current'
#shotnums = [['834', '835', '836'], ['831', '832', '833'], ['828', '829', '830'], \
#    ['825', '826', '827'], ['822', '823', '824'], ['819', '820', '821'], ['815', '816', '817', '818']]
#descript = ['-90V', '-75V', '-60V', '-45V', '-30V', '-15V', '0V']
#vme_plot_diag_for_shots(shotnums, diag, descript)




#diag = 'current'
#shotnums = [['834', '835', '836'], ['828', '829', '830'], ['822', '823', '824'], \
#['815', '816', '817', '879', '880', '881', '904', '905', '906', '907', '843', '844', '845', '846'], \
#    ['882', '883', '884', '899', '900', '901', '902', '903', '851', '854', '855'], \
#    ['885', '886', '887', '895', '896', '897', '860', '861', '863'], \
#    ['888', '889', '890', '891', '892', '893', '894', '869', '870', '871', '872']]
#descript = ['-90V', '-60V', '-30V', '0V', '30V', '60V', '90V']
#vme_plot_diag_for_shots(shotnums, diag, descript)






#diag = 'current'
## Probe has been lowered.
#shotnums = ['242', '243', '244', '245', '246', ['242', '243', '244', '245', '246']]
#shotnums = ['247', '248', '249', ['247', '248', '249']]
#shotnums = ['250', '252', '253', ['250', '252', '253']]
#shotnums = ['254', '255', '256', ['254', '255', '256']]
#shotnums = ['257', '258', '259', '260', ['257', '258', '259', '260']]
#
#
#descript = ['0V', '50V', '100V', '150V', '200V']
#vme_plot_diag_for_shots(shotnums, diag)#, descript)




#diag = 'tek_hv'
#shotnums = [['879', '880', '881', '904', '905', '906', '907', '843', '844', '845', '846'], \
#    ['882', '883', '884', '899', '900', '901', '902', '903', '851', '854', '855'], \
#    ['885', '886', '887', '895', '896', '897', '860', '861', '863'], \
#    ['888', '889', '890', '891', '892', '893', '894', '869', '870', '871', '872']]
#descript = ['0V', '30V', '60V', '90V']
#vme_plot_diag_for_shots(shotnums, diag, descript)





# Probe has been lowered.
#shotnums = [['879', '880', '881'], ['882', '883', '884'], \
#            ['885', '886', '887'], \
#            ['888', '889', '890']]
#descript = ['0V', '30V', '60V', '90V']
#plot_sol_mpa_for_shots(shotnums, descript)

#plt.figure()
#
#shotnums = ['888']
#plot_sol_mpa_for_shots(shotnums)





### Probe has been lowered.
#shotnums = [['904', '905', '906', '907'], ['899', '900', '901', '902', '903'], \
#             ['895', '896', '897'], ['891', '892', '893', '894']]
#descript = ['0V', '30V', '60V', '90V']
#plot_sol_mpa_for_shots(shotnums, descript)


#shotnums = [['843', '844', '845', '846'], ['847', '848', '849'], \
#            ['851', '854', '855'], \
#            ['856', '857', '858'], ['860', '861', '863'], \
#            ['864', '865', '867']]
#descript = ['0V', '15V', '30V', '45V','60V', '75V', '90V']
#plot_sol_mpa_for_shots(shotnums, descript)




#shotnums=['843', '844', '845', '846', ['843', '844', '845', '846']]
#plot_sol_mpa_for_shots(shotnums)






















#mpa_data = vme_avg_sig(['844'], diag='sol_mpa')
#
#time = mpa_data['time']
#bdot = (mpa_data['bx'], mpa_data['by'], mpa_data['bz'])
#b = get_b_from_bdot(time, bdot)
#plt.plot([0, 30], [0, 0], '-k')
#plt.plot(time, b[0], color='g')
#plt.plot(time, b[1], color='b')
#plt.plot(time, b[2], color='r')
#plt.xlim(15, 30)
#plt.ylim(-600, 600)



#
#vme_plot_diagnostic(time, b, diag='sol_mpa.int')





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
#vme_plot_diag_for_shots(shotnums, diag='sol_mpa', descript=descript)
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
