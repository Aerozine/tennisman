import numpy as np 
import matplotlib.pyplot as plt 
from numpy.polynomial import Polynomial as poly 
"""def bissection(f,x0,x1,tol):
    status=0
    a=f(x0)
    b=f(x1)
    if(a>0 and 0>b):
        bissection(f,x1,x0,tol)
    elif(x0==x1):
        status = 1
        return x0
    while(abs(a-b)>tol):
        c=(a+b)/2
        if(c>0 and a > c):
            a=c 
        elif(c<0 and b < c):
            b=c
        elif(not c):
            return c
"""
def bissection(f,x0,x1,tol):
    fx0=f(x0)
    fx1=f(x1)
    while(abs(fx0-fx1)>tol):
    #    print("test")
        tmp = (x0+x1)/2 
        ftmp=f(tmp)
        if(ftmp<0):
            x0=tmp
            fx0=ftmp
        elif(ftmp>0):
            x1=tmp
            fx1=ftmp
        else:
            return tmp
    return(x0)
