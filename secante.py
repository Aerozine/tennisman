import numpy as np
import matplotlib.pyplot as plt 
def secante(f, x0, x1, tol):
    iteration_max=1;
    a=f(x0)
    b=f(x1)
    if b==a:
        return'error',1
    else:
        while abs(b-a)>abs(tol) :
            if b==a:
                return'error',1
            iteration_max+=1
            if iteration_max==100:
                return 'error',-1 
            x1=x1-(b*(x1-x0))/(b-a)
        return b,0
