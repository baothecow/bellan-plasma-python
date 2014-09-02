""" Container of all the different variables """

import os as os

plot_diag_params = {
    ## Rogowski current parameteres
    'current.name': 'Rogowski',
    'current.title': 'Current vs Time',
    'current.ytitle': 'Current (kA)',
    'current.xtitle': 'Time (' + '$\mu$' + 's)',
    'current.xlim': [0, 15],
    'current.ylim': [-80, 20],
    'current.smooth_win': 50,
    'current.subplot.styles': 111,
    
    ## Tektronic HV probe parameters
    'tek_hv.name': 'Tektronic HV',
    'tek_hv.title': 'Voltage vs Time',
    'tek_hv.ytitle': 'Voltage (V)',
    'tek_hv.xtitle': 'Time (' + '$\mu$' + 's)',
    'tek_hv.xlim': [-5, 15],
    'tek_hv.ylim': [-4000, 1000],
    'tek_hv.smooth_win': 50,
    'tek_hv.subplot.styles': 111,

    ## Xiang Zhai's Isolated HV probe parameters
    'iso_hv.name': 'Isolated HV Probe',
    'iso_hv.title': 'Voltage vs Time',
    'iso_hv.ytitle': 'Voltage (V)',
    'iso_hv.xtitle': 'Time (' + '$\mu$' + 's)',
    'iso_hv.xlim': [-5, 15],
    'iso_hv.ylim': [-4000, 1000],
    'iso_hv.smooth_win': 50,
    'iso_hv.subplot.styles': 111,

    ## Collimator probe parameters
    'collimator.name': 'Collimator Signal',
    'collimator.title': 'Voltage vs Time',
    'collimator.ytitle': 'Voltage (V)',
    'collimator.xtitle': 'Time (' + '$\mu$' + 's)',
    'collimator.xlim': [-5, 15],
    'collimator.ylim': [-1, 5],
    'collimator.smooth_win': 50,
    'collimator.subplot.styles': 111,

    ## MPA plot properties.
    'sol_mpa.name': 'Solar MPA',
    'sol_mpa.title': 'Bdot vs time',
    'sol_mpa.ytitle': 'Bdot (V)',
    'sol_mpa.xtitle': 'Time (' + '$\mu$' + 's)',
    'sol_mpa.xlim': [0, 15],
    'sol_mpa.ylim': [-5, 5],
    'sol_mpa.smooth_win': 50,
    'sol_mpa.subplot.styles': ((3, 1, 1), (3, 1, 2), (3, 1, 3)),
    'sol_mpa.subplot.titles': ['Probe 1', ' ', ' '],
    'sol_mpa.subplot.xtitles': [' ', ' ', 'Time (' + '$\mu$' + 's)'],
    'sol_mpa.subplot.ytitles': ['Vx', 'Vy', 'Vz'],
    # Subsection for plotting parameters when integrated.
    'sol_mpa.int.name': 'Solar MPA',
    'sol_mpa.int.title': '',
    'sol_mpa.int.ytitle': 'B (Gauss)',
    'sol_mpa.xtitle': 'Time (' + '$\mu$' + 's)',
    'sol_mpa.int.xlim': [0, 15],
    'sol_mpa.int.ylim': [-500, 1000],
    'sol_mpa.int.smooth_win': 50,
    'sol_mpa.int.subplot.styles': ((3, 1, 1), (3, 1, 2), (3, 1, 3)),
    'sol_mpa.int.subplot.titles': ['Probe 1', ' ', ' '],
    'sol_mpa.int.subplot.xtitles': [' ', ' ', 'Time (' + '$\mu$' + 's)'],
    'sol_mpa.int.subplot.ytitles': ['Bx (G)', 'By ( G)', 'Bz (G)'],
                                    
    ## Hall probe plot properties
    'hall.title': 'Hall voltage vs Time',
    'hall.xlim': [0, 20000],
    'hall.ylim': [-.08, .02],
    'hall.smooth_win': 50,
    'hall.subplot.styles': ((3, 1, 1), (3, 1, 2), (3, 1, 3)),
    'hall.subplot.titles': ['Sensor Output', ' ', ' '],
    'hall.subplot.xtitles': [' ', ' ', 'Time (' + '$\mu$' + 's)'],
    'hall.subplot.ytitles': ['Vx', 'Vy', 'Vz'],
    ## Subsection for plotting hall magnetic reading instead of straight hall voltage.
    'hall.b.title': 'Magnetic Field vs Time',
    'hall.b.xlim': [-5000, 15000],
    'hall.b.ylim': [-.08, .02],
    'hall.b.smooth_win': 50,
    'hall.b.subplot.styles': ((3, 1, 1), (3, 1, 2), (3, 1, 3)),
    'hall.b.subplot.titles': ['Sensor Output', ' ', ' '],
    'hall.b.subplot.xtitles': [' ', ' ', 'Time (' + '$\mu$' + 's)'],
    'hall.b.subplot.ytitles': ['Bx (G)', 'By (G)', 'Bz (G)'],
                               
    ## Generic scalar diagnostic parameteres
    'generic.name': 'Generic Diagnostic',
    'generic.title': 'Generic Diagnostic vs Time',
    'generic.ytitle': 'Voltage (V)',
    'generic.xtitle': 'Time (' + '$\mu$' + 's)',
    'generic.xlim': [0, 20000],
    'generic.ylim': [-80, 20],
    'generic.smooth_win': 50,
    'generic.subplot.styles': 111,


    ## General (default) parameters.
    'gen.color': 'k',
    'gen.ls': '-',
    'gen.title': 'Generic plot title',
    'gen.xtitle': 'Generic x title',
    'gen.ytitle': 'Generic y title',
    'gen.xlim': [-5, 15],
    'gen.ylim': (-40, 40),
    'gen.thin_ln_width': .5,
    'gen.med_ln_width': 1,
    'gen.thick_ln_width': 2,
    'gen.smooth_win': 50,
    'gen.shotnum': '-999',
    # 'gen.vector.label': 'Probe 1',    # Used in labeling vectors plots.
    'gen.subplot.scalar': [111],            # No generic sub plot.
    'gen.subplot.vector': [311, 312, 313],
    'gen.include.raw': True,                # Default is to include raw.
    'gen.label.current.plot': True,         # Sets whether to label a plot or not.
    'gen.subplot.ytitles': [' ', ' ', ' '],
    'gen.subplot.xtitles': [' ', ' ', 'Time (' + '$\mu$' + 's)'],
    'gen.subplot.titles': ['x', 'y', 'z'],
    'gen.multiprobe.label': 'Probe 1',
    'gen.tick.off': False,
    'gen.custom.limit.x': True,     # If set to True, plotting will use user limits.
    'gen.custom.limit.y': False,
    'gen.shotnum_legend': True,     # Set to false if you don't want to see the legend containing shot numbers.

    ## Default colors  (Use of brewer colors -- colorbrew2.org) 
    'gen.color0': '#1f78b4',
    'gen.color1': '#33a02c',
    'gen.color2': '#e31a1c',
    'gen.color3': '#ff7f00',
    'gen.color4': '#6a3d9a',
    'gen.color5': '#b15928',
    'gen.color6': '#a6cee3',
    'gen.color7': '#b2df8a',  
    'gen.color8': '#fb9a99',
    'gen.color9': '#fdbf6f',
    'gen.color10': '#cab2d6',
    'gen.color11': '#ffff99',
    'gen.color12': '#000000'
}     




## Dict containing the parameters associated with a diagnostic's VME parameters.
#       row: number of rows in VME file.
#       cols: standard # of elements saved.
#       ind: index within the VME file. In 'iv' files, ind=2 for current.
#            for vector diagnostics, this is a placeholder variable.
#       vme: name saved under vme.
#       datatype: vector vs scalar diagnostics.
#       numprobes: number of probes associated with the diagnostics.
#       components: denotes the components of the diagnostics and how they
#           are saved within the VME.
#       corr.threshold: may the code isolate trials which are diff from avg.
diag_params = {
    'current.rows': 3,
    'current.cols': 8192,
    'current.ind': 2,
    'current.vme': 'current',
    'current.numprobes': 1,
    'current.datatype' : 'scalar',
    'current.corr.threshold': 0.95,
    'tek_hv.rows': 3,
    'tek_hv.cols': 8192,
    'tek_hv.ind': 1,
    'tek_hv.vme': 'tek_hv',
    'tek_hv.numprobes': 1,
    'tek_hv.datatype' : 'scalar',
    'tek_hv.corr.threshold': 0.90,
    'iso_hv.rows': 2,
    'iso_hv.cols': 8192,
    'iso_hv.ind': 1,
    'iso_hv.vme': 'iso_hv',
    'iso_hv.numprobes': 1,
    'iso_hv.datatype': 'scalar',
    'iso_hv.corr.threshold': 0.90,
    'collimator.rows': 2,
    'collimator.cols': 8192,
    'collimator.ind': 1,
    'collimator.vme': 'optical_trigger',
    'collimator.datatype': 'scalar',
    'collimator.corr.threshold': 0.90,
    'sol_mpa.rows': 5,   # Each file contains info on time and 4 channels.
    'sol_mpa.cols': 16384,
    'sol_mpa.ind': 1,
    'sol_mpa.components': ['bx', 'by', 'bz'],
    'sol_mpa.bx.ind': 1,    # All three components are 1 because the sol_mpa
    'sol_mpa.by.ind': 1,    # stores multiple probe data within 1 file
    'sol_mpa.bz.ind': 1,    # instead of multiple components.
    'sol_mpa.vme': 'sol_mpa_bx',     # Default value is bx
    'sol_mpa.numprobes': 4,
    'sol_mpa.datatype': 'vector',
    'sol_mpa.int.datatype': 'vector',
    'sol_mpa.corr.threshold': 0.5,
    'hall.rows': 4,
    'hall.cols': 65536,
    'hall.ind': 1,   # Default behavior is to just plot the Bx value.
    'hall.components': ['bx', 'by', 'bz'],
    'hall.bx.ind': 1,   
    'hall.by.ind': 2,   
    'hall.bz.ind': 3,   
    'hall.vme': 'hall_bx',     # Default value is bx
    'hall.numprobes': 1,       # Set between 1-5 depending on sensors A-E used.
    'hall.datatype': 'vector',
    'hall.corr.threshold': 0.9,   
    'hall.sensor': 'A',         # Default hall sensor used is sensor A.
    'hall.b.datatype': 'vector',
    
    # Generic diagnostics
    'generic.rows': 2,        # Generic is used to quickly read data from a generic scalar diagnostic.
    'generic.cols': 65536,
    'generic.ind': 1,
    'generic.vme': 'generic',
    'generic.numprobes': 1,
    'generic.datatype' : 'scalar',
    'generic.corr.threshold': 0.95,
    'generic.path': os.sep + 'strap_rogowski_',
    
    # General traits across all diagnostics.
    'gen.probenum': 1,
    'gen.corr.lower.ind': 1450,
    'gen.corr.upper.ind': 3000,
    'gen.presmooth': False,
    'gen.presmooth.const': 100,
    'gen.prefilter': False,
    'gen.filter.application': '',
    'gen.set.breakdown.time.to.zero': True,
    'gen.trim': False,              # If ncessary, trim the data to within a certain time interval.
    'gen.trim.low.limit': -10,      # lower limit in microseconds.
    'gen.trim.range': 7000,          # Number of points to look after the lower limit.
    'gen.minmaxtechnique': 'std',   # Can be 'std' or 'minmax'
}



## Dict containing various path variables associated with solar singleloop
# experiments.

if os.sep == '/':
    exp_paths = {
    # Experiment
    'EXP':'NOTSET',

    # General parameters
    'gen.ENVIR': 'C:\\Program Files\\ITT\\IDL\\IDL81\\bin\\bin.x86_64\\',
    'gen.PY_LIB_PATH': '/home/bao/GitHub/bellan-plasma-python/',
    # Singleloop parameters
    'singleloop.IDL_LIB_PATH': '/E/programs/idl/singleloop_lib\\',
    'singleloop.IDL_VME_PATH': '/E/data/singleloop/singleloop_VME/data/',
    'singleloop.METADATA': '/E/data/singleloop/singleloop_metadata/',
    # Solar parameters
    'solar.IDL_LIB_PATH': '/E/programs/idl/solar_lib/',
    'solar.IDL_VME_PATH': '/E/data/solar/solar_accretion/data/',
    # Hall parameters
    'hall.IDL_LIB_PATH': '/E/programs/idl/singleloop_lib/hall_project/',
    'hall.IDL_VME_PATH': '/E/data/singleloop/singleloop_VME/hall/',
    # Imacon parameters
    'singleloop.REDUCED_PATH': '/E/data/singleloop/singleloop_imacon/reduced/',
    'singleloop.IMACON_PATH': '/F/data/singleloop_imacon/data/'
    }
elif os.sep == '\\':
    exp_paths = {
    # Experiment
    'EXP':'NOTSET',
    # General parameters
    'gen.ENVIR': 'C:\\Program Files\\ITT\\IDL\\IDL81\\bin\\bin.x86_64\\',
    'gen.PY_LIB_PATH': 'C:\\Users\\Bao\\Documents\\GitHub\\bellan-plasma-python\\',
    # Singleloop parameters
    'singleloop.IDL_LIB_PATH': 'E:\\programs\\idl\\singleloop_lib\\',
    'singleloop.IDL_VME_PATH': 'E:\\data\\singleloop\\singleloop_VME\\data\\',
    'singleloop.METADATA': 'E:\\data\\singleloop\\singleloop_metadata\\',
    # Solar parameters
    'solar.IDL_LIB_PATH': 'E:\\programs\\idl\\solar_lib\\',
    'solar.IDL_VME_PATH': 'E:\\data\\solar\\solar_accretion\\data\\',
    # Hall parameters
    'hall.IDL_LIB_PATH': 'E:\\programs\\idl\\singleloop_lib\\hall_project\\',
    'hall.IDL_VME_PATH': 'E:\\data\\singleloop\\singleloop_VME\\hall\\',
    # Imacon parameters
    'singleloop.REDUCED_PATH': 'E:\\data\\singleloop\\singleloop_imacon\\reduced\\',
    'singleloop.IMACON_PATH': 'F:\\data\\singleloop_imacon\\data\\'
    }    

    

#exp_paths = {
#    # Experiment
#    'EXP':'NOTSET',
#    # General parameters
#    'gen.ENVIR': 'C:\\Program Files\\ITT\\IDL\\IDL81\\bin\\bin.x86_64\\',
#    'gen.PY_LIB_PATH': 'C:\\Users\\Bao\\Documents\\GitHub\\bellan-plasma-python\\',
#    # Singleloop parameters
#    'singleloop.IDL_LIB_PATH': 'E:\\programs\\idl\\singleloop_lib\\',
#    'singleloop.IDL_VME_PATH': 'E:\\data\\singleloop\\singleloop_VME\\data\\',
#    'singleloop.METADATA': 'E:\\data\\singleloop\\singleloop_metadata\\',
#    # Solar parameters
#    'solar.IDL_LIB_PATH': 'E:\\programs\\idl\\solar_lib\\',
#    'solar.IDL_VME_PATH': 'E:\\data\\solar\\solar_accretion\\data\\',
#    # Hall parameters
#    'hall.IDL_LIB_PATH': 'E:\\programs\\idl\\singleloop_lib\\hall_project\\',
#    'hall.IDL_VME_PATH': 'E:\\data\\singleloop\\singleloop_VME\\hall\\',
#    # Imacon parameters
#    'singleloop.REDUCED_PATH': 'E:\\data\\singleloop\\singleloop_imacon\\reduced\\',
#    'singleloop.IMACON_PATH': 'F:\\data\\singleloop_imacon\\data\\'
#}    


#exp_paths = {
#    # Experiment
#    'EXP':'NOTSET',
#
#    # General parameters
#    'gen.ENVIR': 'C:\\Program Files\\ITT\\IDL\\IDL81\\bin\\bin.x86_64\\',
#    'gen.PY_LIB_PATH': '/home/bao/GitHub/bellan-plasma-python/',
#    # Singleloop parameters
#    'singleloop.IDL_LIB_PATH': '/E/programs/idl/singleloop_lib\\',
#    'singleloop.IDL_VME_PATH': '/E/data/singleloop/singleloop_VME/data/',
#    'singleloop.METADATA': '/E/data/singleloop/singleloop_metadata/',
#    # Solar parameters
#    'solar.IDL_LIB_PATH': '/E/programs/idl/solar_lib/',
#    'solar.IDL_VME_PATH': '/E/data/solar/solar_accretion/data/',
#    # Hall parameters
#    'hall.IDL_LIB_PATH': '/E/programs/idl/singleloop_lib/hall_project/',
#    'hall.IDL_VME_PATH': '/E/data/singleloop/singleloop_VME/hall/',
#    # Imacon parameters
#    'singleloop.REDUCED_PATH': '/E/data/singleloop/singleloop_imacon/reduced/',
#    'singleloop.IMACON_PATH': '/F/data/singleloop_imacon/data/'
#}

