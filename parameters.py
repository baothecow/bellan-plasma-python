""" Container of all the different variables """



plot_diag_params = {
    ## Rogowski current parameteres
    'current.name': 'Rogowski',
    'current.title': 'Current vs time',
    'current.ytitle': 'Current (kA)',
    'current.xtitle': 'Time (' + '$\mu$' + 's)',
    'current.xlim': [10, 30],
    'current.ylim': [-40, 40],
    'current.smooth_win': 50,
    
    ## Tektronic HV probe parameters
    'tek_hv.name': 'Tektronic HV',
    'tek_hv.title': 'Voltage vs time',
    'tek_hv.ytitle': 'Voltage (V)',
    'tek_hv.xtitle': 'Time (' + '$\mu$' + 's)',
    'tek_hv.xlim': [10, 30],
    'tek_hv.ylim': [-4000, 1000],
    'tek_hv.smooth_win': 50,

    ## Xiang Zhai's Isolated HV probe parameters
    'iso_hv.name': 'Isolated HV Probe',
    'iso_hv.title': 'Voltage vs time',
    'iso_hv.ytitle': 'Voltage (V)',
    'iso_hv.xtitle': 'Time (' + '$\mu$' + 's)',
    'iso_hv.xlim': [10, 30],
    'iso_hv.ylim': [-4000, 1000],
    'iso_hv.smooth_win': 50,

    ## MPA plot properties.
    'sol_mpa.name': 'Solar MPA',
    'sol_mpa.title': 'Magnetic Field vs time',
    'sol_mpa.ytitle': 'B (Gauss)',
    'sol_mpa.xtitle': 'Time (' + '$\mu$' + 's)',
    'sol_mpa.xlim': [10, 30],
    'sol_mpa.ylim': [-1000, 1000],
    'sol_mpa.smooth_win': 50,

    ## Default parameters.
    'gen.color': 'k',
    'gen.ls': '-',
    'gen.title': 'Generic plot title',
    'gen.xtitle': 'Generic x title',
    'gen.ytitle': 'Generic y title',
    'gen.xlim': (10, 30),
    'gen.ylim': (-40, 40),
    'gen.thin_ln_width': .5,
    'gen.med_ln_width': 1,
    'gen.thick_ln_width': 2,
    'gen.smooth_win': 50,
    'gen.shotnum': '-999',

    ## Default colors
    'gen.color0': 'r',
    'gen.color1': 'b',
    'gen.color2': 'g',
    'gen.color3': 'c',
    'gen.color4': 'm',
    'gen.color5': 'y',
    'gen.color6': 'k'
}     




## Dict containing the parameters associated with diagnostics VME files.
#       row: number of rows in VME file.
#       cols: standard # of elements saved.
#       ind: index within the VME file. In 'iv' files, ind=2 for current.
#       vme: name saved under vme.
diag_params = {
    'current.rows': 3,
    'current.cols': 8192,
    'current.ind': 2,
    'current.vme': 'iv',
    'current.datatype' : 'scalar',
    'current.numprobes': 1,
    'tek_hv.rows': 3,
    'tek_hv.cols': 8192,
    'tek_hv.ind': 1,
    'tek_hv.vme': 'iv',
    'tek_hv.numprobes': 1,
    'current.datatype' : 'scalar',
    'iso_hv.rows': 2,
    'iso_hv.cols': 8192,
    'iso_hv.ind': 1,
    'iso_hv.vme': 'HV',
    'iso_hv.numprobes': 1,
    'current.datatype': 'scalar',
    'sol_mpa.rows': 5,
    'sol_mpa.cols': 16384,
    'sol_mpa.ind': 1,
    'sol_mpa.components': ['bx', 'by', 'bz'],
    'sol_mpa.vme': 'sol_mpa_bx',     # Default value is bx
    'sol_mpa.numprobes': 4,
    'sol_mpa.datatype': 'vector'
    
##    'sol_mpa.vme.x' : 'sol_mpa_bx',
##    'sol_mpa.vme.y' : 'sol_mpa_by',
##    'sol_mpa.vme.z' : 'sol_mpa_bz'
}
