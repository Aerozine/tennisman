import numpy as np
import matplotlib.pyplot as plt 
def secante(f, x0, x1, tol):
    iteration_max=1
    while iteration_max<100:
        iteration_max+=1
        a=f(x0)
        b=f(x1)
        if b==a :
            return'error',1
        if abs(b-a)< tol :
            return x1,0
        else:
            x_new=x1-b*(x1-x0)/(b-a)
            x0,x1=x1,x_new
    return 'error',-1


