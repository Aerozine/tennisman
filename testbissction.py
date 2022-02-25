import bissection
import numpy as np
from matplotlib import pyplot as plt
from RechercheRacine import fun 
from numpy.polynomial import Polynomial as poly 
import random
x=np.linspace(-10,10,150)

def checkifgood(tol,roo,b):
    for i in range(0,len(roo)):
        if (abs(roo[i]-b)<=tol*10):
            return 1
    print(tol , roo, b ) 





"""arr=f.roots
realroot=arr.real[abs(arr.imag)<1e-5]
plt.plot(realroot,np.zeros_like(realroot),"or")
"""

tol=0.00001

for i in range (1,1000):
    c=fun.ction(6)
    r=np.roots(c)
    #print(b)
    f=poly(c)
    plt.plot(x,f(x),"g")
    roo=[]
    array=f.roots()
    for i in range (0,len(array)):
        if (array[i].imag < 1e-5):
            roo.append(array[i].real) 
    b=bissection.bissection(poly(c),roo[0]-1000*random.random(),roo[0]+1000*random.random(),tol)
    #print(roo)
    checkifgood(tol,roo,b)
#plt.plot(roo , np.zeros_like(roo),"or")
#plt.plot(b,np.zeros_like(b),"ob")
#plt.show()

