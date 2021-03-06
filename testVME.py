from vme_plot_specific import vme_plot_diag_for_shots, plot_sol_mpa_for_shots
from parameters import diag_params, plot_diag_params, exp_paths
from vme_analyze import vme_unflatten_list, vme_get_breakdown_time
from DictOfBreakdowns import DictOfBreakdowns


## Correlation between sol_mpa and main bank charging voltage
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#plot_diag_params['gen.shotnum_legend'] = True
diag = 'iso_hv'
start=3000
shotnums = [map(str, range(start, start+10))]
#descript = ['3kV', '3.5kV', '4kV', '4.5kV', '5kV']
#plot_sol_mpa_for_shots(shotnums, num_probe=4)

vme_plot_diag_for_shots(shotnums, diag, extra='indiv_signals')


#
### Current trace while varying the amount of gas injected into chamber.
#diag = 'current'
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#plot_diag_params['gen.shotnum_legend'] = True
#shotnums = vme_unflatten_list(map(str, range(1569, 1573)+range(1592, 1596)))
#vme_plot_diag_for_shots(shotnums, diag)





### Adding and removing times from breakdown time
#
#root_path = exp_paths['singleloop.METADATA']
#myDictOfBreakdowns = DictOfBreakdowns(root_path)
#for shotnum in range(389, 2029):
#    breakdown_time = vme_get_breakdown_time(str(shotnum))    
#    myDictOfBreakdowns.set_breakdown_time(shotnum, breakdown_time)
#    print (shotnum, myDictOfBreakdowns.get_breakdown_time_date(shotnum))
#myDictOfBreakdowns.pickle_dump()
#
#myDictOfBreakdowns = DictOfBreakdowns(root_path)
#myDictOfBreakdowns.print_all_keys()


### Current trace while varying the amount of gas injected into chamber.
#diag = 'current'
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#plot_diag_params['gen.shotnum_legend'] = False
#shotnums = [['2065'], ['2094'], ['2124'], ['2074'], ['2104'], ['2084'], ['2114']]
#descript = ['0', '30V', '45V', '60V', '75V', '90V', '105V']
#vme_plot_diag_for_shots(shotnums, diag, descript, extra='indiv_signals')
#plt.xlim(0, )

### Current trace while varying the amount of gas injected into chamber.
#diag = 'current200'
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#plot_diag_params['gen.shotnum_legend'] = False
#shotnums = [map(str, range(510, 516)), map(str, range(504, 510)), map(str, range(516, 522)), \
#            map(str, range(522, 528)), map(str, range(528, 534))]
#descript = ['Gas: 450V', 'Gas: 500V', 'Gas: 550V', 'Gas: 600V', 'Gas: 650V']
#vme_plot_diag_for_shots(shotnums, diag, descript, extra='indiv_signals')
#plt.xlim(0, )


### Vary bias fields on Apr 2014
###
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#plot_diag_params['gen.shotnum_legend'] = True
#diag = 'current'
#shotnums = [map(str, range(1430, 1433)), map(str, range(1433, 1436)), map(str, range(1436, 1439)), \
#            map(str, range(1439, 1442)), map(str, range(1442, 1445))]
#descript = ['200/200', '100/200', '50/200', '25/200', '0/200']
#
##shotnums = [map(str, [1445]), map(str, range(1446, 1449)), map(str, range(1449, 1452)), \
##            map(str, range(1452, 1455)), map(str, range(1455, 1458))]
##descript = ['200/200', '200/100', '200/50', '200/25', '200/0']
#
##plot_sol_mpa_for_shots(shotnums, descript=descript, num_probe=4)
#
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')



### Correlation between sol_mpa and main bank charging voltage
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#plot_diag_params['gen.shotnum_legend'] = True
#diag = 'current'
#shotnums = [map(str, range(1002, 1005)), map(str, range(1005, 1008)), map(str, range(1008, 1011)), map(str, range(1011, 1014)), map(str, range(1014, 1017))]
#descript = ['3kV', '3.5kV', '4kV', '4.5kV', '5kV']
##plot_sol_mpa_for_shots(shotnums, descript=descript, num_probe=4)

#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')

## Comparing different stuffing fluxes.
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag_params['gen.minmaxtechnique'] = 'std'
#plot_diag_params['gen.shotnum_legend'] = False
#diag = 'current'
#shotnums = [map(str, range(1053, 1060)), map(str, range(1017, 1025))]
#descript = ['Top:100V\nBot:200V', 'Top:200V\nBot:200V']
#shotnums = [map(str, range(1044, 1047)), map(str, range(1050, 1053)), map(str, range(1025, 1028))]
#descript = ['Top:0V\nBot:200V', 'Top:100V\nBot:200V', 'Top:200V\nBot:200V']
#shotnums = [map(str, range(1044, 1047)), map(str, range(1047, 1050)), map(str, range(1050, 1053)), map(str, range(1025, 1028))]
#descript = ['Top:0V\nBot:200V', 'Top:50V\nBot:200V', 'Top:100V\nBot:200V', 'Top:200V\nBot:200V']
#
#shotnums = [map(str, range(937, 939)), map(str, range(939, 941))]
#descript = ['0/200', '100/200']
#
#shotnums = [map(str, range(1050, 1053)), map(str, range(939, 941))]
#descript = ['100/200', '100/200']
#
#
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')

#plot_diag_params['gen.shotnum_legend'] = True
#shotnums = vme_unflatten_list(map(str, range(1397, 1407)))
#vme_plot_diag_for_shots(shotnums, diag, extra='indiv_signals')


#
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'current'
#shot_arr = [map(str, range(1530, 1538)), map(str, range(1928, 1937))]
##shot_arr = ['1957', '1958', '1959', '1960']
##shotnums = [map(str, range(1530, 1538)), map(str, range(1928, 1937)), map(str, range(1553, 1559))]
#shotnums = [map(str, range(1530, 1538)), map(str, range(1543, 1549))]
##shotnums = vme_unflatten_list(shot_arr)
#vme_plot_diag_for_shots(shotnums, diag, extra='indiv_signals')



## Code for comparing two different diagnostics.
#from parameters import diag_params
#from vme_analyze import vme_avg_scalar_sig
#from cookb_signalsmooth import smooth
#import numpy as np
#
#
#diag_params['gen.prefilter'] = False
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'current'
##shotnums = map(str, range(1530, 1539))
#shotnums = ['1572']
#data = vme_avg_scalar_sig(shotnums, diag, extra='indiv_signals')
#(time, current1) = (data[0], data[1])
#diag = 'current'
#shotnums = map(str, range(1543, 1550))
#shotnums = ['1573']
#data2 = vme_avg_scalar_sig(shotnums, diag, extra='indiv_signals')
#(time2, current2) = (data2[0], data2[1])
#
#
#smoo_cur1 = smooth(current1, 100)
#smoo_cur2 = smooth(current2, 100)
#
#
#plt.figure()
#plt.plot(time, smoo_cur1)
#plt.plot(time, smoo_cur2)
#plt.xlim(-5, 15)
#plt.title('Current vs Time')
#
#print np.max(smoo_cur2)/np.max(smoo_cur1)




## For comparing voltage data.
#from parameters import diag_params
#from vme_analyze import vme_avg_scalar_sig
#
#
#diag_params['gen.prefilter'] = False
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'tek_hv'
#shotnums = ['1397']
#data = vme_avg_scalar_sig(shotnums, diag, extra='indiv_signals')
#(time, volt1) = (data[0], data[1])
#diag = 'iso_hv'
#shotnums = ['1397']
#data2 = vme_avg_scalar_sig(shotnums, diag, extra='indiv_signals')
#(time, volt2) = (data2[0], data2[1])
#
#plt.figure()
#plt.plot(time, volt1)
#plt.plot(time, volt2)
#plt.xlim(-5, 15)
#plt.ylim(-3000, 500)


#from parameters import diag_params
#from vme_plot_specific import vme_plot_diag_for_shots
#
#
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'current'
#shotnums = [map(str, range(1489, 1495)), map(str, range(1495, 1508)), map(str, range(1508, 1517))]
#vme_plot_diag_for_shots(shotnums, diag, extra='indiv_signals')



#from vme_plot_specific import vme_plot_diag_for_shots
#from parameters import diag_params
#
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'current'
#shotnums = [map(str, range(1530, 1539)), map(str, range(1520, 1526) + range(1527, 1530)), \
#            map(str, range(1508, 1520)), map(str, range(1495, 1508)), map(str, range(1488, 1495))]
#descript = ['No extra inductance', 'Small extra', 'Med extra', 'Large extra', 'Maximum extra']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')


## Rogowski reading from hall sensors.
 
### Make sure to update foldername.pro within the hall sensor directory so that it contains the information
### found within hallfoldernamcaitilnduncan125@gmail.come.por
#from parameters import exp_paths
#from parameters import diag_paracaitilnduncan125@gmail.comms
#from vme_plot_specific import vme_plot_diag_for_shots
#
#exp_paths['EXP'] = 'hall'
#diag_params['generic.path'] = '\\strap_rogowski_'
#diag_params['gen.set.breakdown.time.to.zero'] = False     # No breakdown of plasma for hall diagnostics.
#diag_params['gen.corr.lower.ind'] = 10000                  # Set correlation index for the large VME data files for hall data.
#diag_params['gen.corr.upper.ind'] = 40000caitilnduncan125@gmail.com
#diag_params['gen.trim'] = False
#diag_params['gen.presmooth'] = False
#diag = 'generic'
#shotnums = [['306'], ['315'], ['321'], ['327']]
#shotnums = [['321'], ['339'], ['345'], ['351']] 
#shotnums = [['357'], ['363'], ['369'], ['375']]
#shotnums = [['383'], ['389'], ['396'], ['402']]
#shotnums = [['408'], ['414'], ['420'], ['430']]
#shotnums = [['432'], ['438'], ['444'], ['449'], ['455']]
#shotnums = [['303'], ['305'], ['306'], ['307'], ['309'], ['310'], ['313'], ['314'], ['315'], ['316'] ]
#vme_plot_diag_for_shots(shotnums, diag, extra='indiv_signals')




 
### Hall sensor -- 
# 
### Make sure to update foldername.pro within the hall sensor directory so that it contains the information
### found within hallfoldername.por
#from parameters import diag_params
#from vme_plot_specific import *
#
#exp_paths['EXP'] = 'hall'
#diag_params['gen.set.breakdown.time.to.zero'] = True     # No breakdown of plasma for hall diagnostics.
#diag_params['gen.corr.lower.ind'] = 10000                  # Set correlation index for the large VME data files for hall data.
#diag_params['gen.corr.upper.ind'] = 30000
#diag_params['gen.trim'] = False
#diag_params['gen.presmooth'] = True
#diag_params['gen.prefilter'] = False
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#shotnums = [map(str, range(357, 359)), map(str, range(396, 398))]
#descript=['With Plates', 'Without Plates']
#plot_hall_for_shots(shotnums, descript=descript, sensor='C', extra='indiv_signals')xp_paths





#### Plot the diagnostics for different configurations of bias fields.
#diag_params['gen.trim'] = True
#diag_params['gen.presmooth'] = False
#diag_params['gen.prefilter'] = False
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#plot_diag_params['gen.custom.limit.y'] =  True
#plot_diag_params['sol_mpa.xlim'] = [0, 10]
#plot_diag_params['sol_mpa.ylim'] = [-5, 5]
#diag = 'sol_mpa'
#shotnums = [map(str, range(1025, 1028)), map(str, range(1034, 1038)), map(str, range(1031, 1034)), map(str, range(1028, 1031)), map(str, range(1038, 1041))]
#descript = ['200V/200V', '200V/100V', '200V/50V', '200V/0V', '200V/400V']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')
#shotnums = [map(str, range(1025, 1028)), map(str, range(1050, 1053)), map(str, range(1047, 1050)), map(str, range(1044, 1047))]
#descript = ['200V/200V', '100V/200V', '50V/200V', '0V/200V']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')
#shotnums = [map(str, range(1025, 1028)), map(str, range(1028, 1031)), map(str, range(1044, 1047)), map(str, range(1041, 1044))]
#descript = ['200V/200V', '200V/0V', '0V/200V', '0V/400V']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')




#### Comparing the sol_mpa for different main bank voltages.
#diag_params['gen.trim'] = True
#diag_params['gen.presmooth'] = False
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'sol_mpa'
#shotnums = [['1002', '1003', '1004'], ['1005', '1006', '1007'], ['1008', '1009', '1010'], \
#['1011', '1012', '1013'], ['1014', '1015', '1016']]
#descript = ['3kV', '3.5kV', '4kV', '4.5kV', '5kV']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')

### Comparing the solar_mpa signal for shots with a spike in current trace vs no spike in current trace.
#diag_params['gen.trim'] = True
#
#diag_params['gen.presmooth'] = False
#diag_params['gen.prefilter'] = False
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'sol_mpa'
#shotnums = [['1399', '1407', '1411', '1416', '1417', '1419', '1421'], ['1398', '1400', '1403', '1410', '1415', '1418']]
#descript = ['Spiky shots', 'Regular shots']
##vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')
#plot_sol_mpa_for_shots(shotnums, descript=descript)







#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'sol_mpa'
#shotnums = [map(str, range(1397, 1407)), map(str, range(1407, 1414)), \
#            map(str, range(1414, 1419)), map(str, range(1427, 1430))] 
##shotnums = [['1397', '1398'], ['1407'], ['1414'], ['1427']]
#descript = ['First series of shots', 'Waited 1 hr', 'Waited 1 more hr', 'After some 60V shots']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')



#
#shotnums = [map(str, range(1160, 1164)), map(str, range(1198, 1203)), \
#            map(str, range(1219, 1224)), map(str, range(1300, 1304)), \
#            map(str, range(1307, 1314)), ['1194'], \
#            map(str, range(1129, 1132)), ['1159']]
#            
#descript = ['1/25/14', '2/06/14 - Early', '2/06/14 - Later', '2/10/14 - Early', \
#             '2/10/14 - Later', '1/25/14 - Last shot', '1/21/14 - Early', \
#             '1/21/14 - Last shot']
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'current_light_low_pass'
#diag = 'current'
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')
#




#
#Strap0 = range(1248, 1252)
#Strap30 = range(1255, 1258)
#Strap60 = range(1261, 1264)
#Strap90 = range(1258, 1261)
#
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'tek_hv_low_pass'
#diag = 'current'
#shotnums = [map(str, Strap0), map(str, Strap30), map(str, Strap60), map(str, Strap90)]
#descript = ['0V', '30V', '60V', '90V']
#vme_plot_diag_for_shots(shotnums, diag, descript=descript, extra='indiv_signals')






#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'heavy_current_low_pass'
#diag = 'current'
#shotnums = [map(str, range(510, 516)), map(str, range(504, 510)), map(str, range(516, 522)), \
#map(str, range(522, 528)), map(str, range(528, 534))]
#descript = ['Gas: 450V', 'Gas: 500V', 'Gas: 550V', 'Gas: 600V', 'Gas: 650V']#, '11/01/13', '10/08/13', '10/07/13', '9/11/13', '9/10/13', '3/13/13', '1/24/13', '1/23/13']
#vme_plot_diag_for_shots(shotnums, diag, descript, band=1, extra='indiv_signals')
#plt.xlim(0, )



#diag_params['gen.prefilter'] = False
#diag_params['gen.filter.application'] = 'heavy_current_low_pass'
#diag = 'tek_hv'
#shotnums = range(1364, 1371)
#shotnums = map(str, shotnums)
#shotnums = vme_unflatten_list(shotnums)
#vme_plot_diag_for_shots(shotnums, diag)
#plt.xlim(0, 15)



#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'heavy_current_low_pass'
#diag = 'current'
#shotnums = [['834', '835', '836'], ['828', '829', '830'], \
#            ['822', '823', '824'], ['815', '816', '817', '818'], \
#            ['879', '880', '881', '904', '905', '906', '907', '843', '844', '845', '846'], \
#            ['882', '883', '884', '899', '900', '901', '902', '903', '851', '854', '855'], \
#            ['885', '886', '887', '895', '896', '897', '860', '861', '863'], \
#            ['888', '889', '890', '891', '892', '893', '894', '869', '870', '871', '872']]
#descript = ['-90V', '-60V', '-30V', '-0V', '0V', '30G', '60G', '90']
#vme_plot_diag_for_shots(shotnums, diag, descript)


#
#diag = 'current'
#shotnums = [map(str, range(510, 516)), map(str, range(504, 510)), map(str, range(516, 522)), \
#map(str, range(522, 528)), map(str, range(528, 534))]
#descript = ['Gas: 450V', 'Gas: 500V', 'Gas: 550V', 'Gas: 600V', 'Gas: 650V']#, '11/01/13', '10/08/13', '10/07/13', '9/11/13', '9/10/13', '3/13/13', '1/24/13', '1/23/13']
#vme_plot_diag_for_shots(shotnums, diag, descript)
#
#plt.xlim(0, )

#
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'heavy_current_low_pass'
#diag = 'current'
#shotnums = ['10100', '10103', '10101', '10105', '10107']
#descript = ['0G', '-150G', '-300G', '-450G', '-600G']
#vme_plot_diag_for_shots(shotnums, diag, descript)



#diag_params['gen.presmooth'] = False
#diag_params['gen.presmooth.const'] = 50

#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'heavy_current_low_pass'
#diag_params['gen.filter.application'] = 'tek_hv_low_pass'

#diag = 'current'
#shots = map(str, (846, 868))
#shotnums = vme_unflatten_list(shots)
#descript = shots
##vme_plot_diag_for_shots(shotnums, diag, descript)
##plt.xlim(0, )
##plot_diag_params['sol_mpa.int.xlim'] = [0, 10]
#plot_sol_mpa_for_shots(shotnums, descript=descript, num_probe=1)







##diag_params['gen.presmooth'] = True
##diag_params['gen.presmooth.const'] = 50
#
#diag_params['gen.prefilter'] = True
#diag_params['gen.filter.application'] = 'heavy_current_low_pass'
##diag_params['gen.filter.application'] = 'tek_hv_low_pass'
#
#diag = 'current'
#shots = map(str, range(1296, 1300))
#shotnums = vme_unflatten_list(shots)
#descript = shots
#vme_plot_diag_for_shots(shotnums, diag, descript)
#plt.xlim(0, )
##plot_diag_params['sol_mpa.int.xlim'] = [0, 10]
##plot_sol_mpa_for_shots(shotnums, descript=descript, num_probe=1)


#
### Code to play around with butterworth digital filter.
#plt.figure()
#
#diag = 'current'
#shotnums = range(803, 804) 
#shotnums = map(str, shotnums)
#data = vme_avg_scalar_sig(shotnums, diag)
#time = data[0]
#signal = data[1]
#
#BACK = 100
#
#zero_index = np.where(time == 0)[0][0]
#end_index = np.where(time > 50)[0][0]
##time = time[zero_index - BACK:end_index]
##signal = signal[zero_index - BACK:end_index]
#
#
#fs = 100e6
#fso2 = fs/2    # Nyquist frequency is half of sampling frequency.
#N, Wn = scisig.buttord(wp=1e5/fso2, ws=4e5/fso2, gpass=0.1, gstop=20)
#b, a = scisig.butter(N, Wn, 'lowpass')
#output_signal = scisig.filtfilt(b, a, signal)
#
#
#plt.plot(time, signal)
#plt.plot(time, output_signal, linewidth=2)
#plt.xlim(0,15)





#
#diag = 'current'
#shotnums = range(806, 807)
#shotnums = map(str, shotnums)
#shotnums = vme_unflatten_list(shotnums)
#vme_plot_diag_for_shots(shotnums, diag)
#plt.xlim(0, 15)



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
