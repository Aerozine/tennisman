import sys 
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
    a = x0 
    b = x1
    fx0=f(x0)
    fx1=f(x1)
    if(fx0):
        return x0
    if(fx1):
        return x1
    if(fx1>fx0)
        return 1
    if((fx1>0 and fx0>0)or(fx1<0 and fx0<0))
        return -1
# error -1 si la racine n existe pas 
#1 si il ne sait pas utiliser la fonction 
# pour vérifier si la fonction converge vers une racine , il suffit de regarder si l absice de la fonction va continuer a décroitre ie que forall p , q f(p) < f(q)
    while(abs(fx0-fx1)>tol):
        tmp = (x0+x1)/2 
        ftmp=f(tmp)
        if(latest==a or latest==b):
            return 
        if(ftmp<0):
            x0=tmp
            fx0=ftmp
            latest=x0
        elif(ftmp>0):
            x1=tmp
            fx1=ftmp
            latest=x1
        else:
            return tmp
    return(latest)
