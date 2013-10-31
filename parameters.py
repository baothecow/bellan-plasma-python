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

    ## Default parameters.
    'gen.color': 'k',
    'gen.title': 'Generic plot title',
    'gen.xtitle': 'Generic x title',
    'gen.ytitle': 'Generic y title',
    'gen.xlim': (10, 30),
    'gen.ylim': (-40, 40),
    'gen.thin_ln_width': .5,
    'gen.med_ln_width': 1,
    'gen.thick_ln_width': .5
}     
