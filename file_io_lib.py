## My file io library
## Mar26, 2013
import array as ar
import numpy as np
import os
import cPickle as pickle

def write_latex(mylist, fname):
    delim = '&'
    fout = open(fname, 'w')
    fout.write("\\begin{tabular}{|c|")
    for k in range(1,len(mylist)):
        fout.write("c|")
    fout.write("}\n")
    for i in range(0,len(mylist)):
        mystr = ""
        for j in range(0,len(mylist[i])-1):
            mystr += str(mylist[i][j]) + delim
        mystr += str(mylist[i][j])
        
        mystr += '\\\\'+'\n'
        mystr += '\hline\n'
        fout.write(mystr)
    fout.write("\end{tabular}")
    fout.close()

def toLatex(fname, delim):
    mydata = np.loadtxt(fname, delimiter=delim,dtype=np.str_,skiprows=1)
    fout = fname.split('.')[0]
    write_latex(mydata, fout + '_latex.txt')

def readVME(fname,cols=8192,rows=2,dtype='f'):
    '''
    Reads data from VME->IDL output files
    fname: full file path,
    cols: number of time steps,
    rows: number variables,
    dtype: desired python data type ('f'-> float)
    '''
    fin = open(fname,'rb')
    a = ar.array('f')
    a.fromfile(fin, cols*rows)
    fin.close()
    ret = []
    for i in range(0,cols*rows,cols):
        ret.append( a[i:i+cols] )
    return np.array(ret)

def fixfile(f0):
    fin = open(f0,'r')
    f = fin.read()
    if f.find('\n') >=0:
        f = f.replace('\r\n','\n')
    else:
        f = f.replace('\r','\n')
    fin.close()
    fout= open(f0,'w')
    fout.write(f)
    fout.close()
    print "fixed"
    
def pickle_dump(obj, filename, path):
    """ Program that pickles an object into a file on the specified path """
    pickle.dump(obj, open(path + filename, "wb"))
    
def pickle_read(path):
    """ Program that unpickles the object given a path to the object """
    return pickle.load(open(path, "rb"))
    
    
        
        
