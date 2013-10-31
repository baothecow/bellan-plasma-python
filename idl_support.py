## This file is motivated by an article found at:
## http://brainimaging.waisman.wisc.edu/~oakes/idl/idl_from_python.html

import subprocess



envir = {'PATH': 'C:\\Program Files\\ITT\\IDL\\IDL81\\bin\\bin.x86_64\\'}

filepath = 'C:\\Users\\Bao\\Documents\\GitHub\\bellan-plasma-python\\'

subprocess.Popen('echo "Hello world!"', shell=True)

subp = subprocess.Popen("idl -e \"@"+filepath+"test.pro\"" ,
        stderr = subprocess.PIPE, stdout = subprocess.PIPE, shell = True, 
        env=envir)

(idl_stdout, idl_stderr) = subp.communicate()



print(idl_stdout)   # for python 2.4, use "print idl_stdout" instead

