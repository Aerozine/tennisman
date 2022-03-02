import numpy as np
import matplotlib.pyplot as plt 
def secante(f, x0, x1, tol):
    iteration_max=0
    a=f(x0)
    b=f(x1)
    if abs(a)<tol :
        return x0,0
    while iteration_max<100:
        if b==a :
            print("il y a une erreur car on ne peut pas diviser par 0 ")
            return [18,1]
        if abs(b)< tol :
            return x1,0
        else:
            x_new=x1-b*(x1-x0)/(b-a)
            x0,x1=x1,x_new
        iteration_max+=1
        a=b
        b=f(x1)
    print("il y a une erreur car la fonction ne converge pas")
    return [18,-1]


