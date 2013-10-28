## VME plotting routines
import matplotlib.pyplot as plt

DEF_TITLE = 'Default title'
DEF_XTITLE = 'Arbitrary units'
DEF_YTITLE = 'Arbitrary units'
DEF_XRANGE = [0,15]
DEF_YRANGE = [0,15]


## Plots VME data.
def vme_plot_current(data, title=DEF_TITLE, xtitle=DEF_TITLE, ytitle=DEF_YTITLE):
    
    plt.plot([1, 2, 3, 4])
    plt.title(title)
    plt.ylabel(ytitle)
    plt.xlabel(xtitle)
    plt.show()


