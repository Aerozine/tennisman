import __main__
import sys
import numpy as np 
import matplotlib.pyplot as plt 
def bissection(f,x0,x1,tol):
    a = x0 
    b = x1
    fx0=f(x0)
    fx1=f(x1)
    if(not fx0):
        return x0,0
    if(not fx1):
        return x1,0
    if(fx1>fx0):
        return bissection(f,x1,x0,tol) 
    if((fx1>0 and fx0>0)or(fx1<0 and fx0<0)or(x1==x0)):
        return 18,1
    latest = None
    while(abs(fx0-fx1)>tol):
        tmp = (x0+x1)/2 
        ftmp=f(tmp)
        plt.plot(tmp,ftmp,"r*")
        if(latest==a or latest==b):
            return 18,-1
        if(ftmp>0):
            x0=tmp
            fx0=ftmp
            latest=x0
        elif(ftmp<0):
            x1=tmp
            fx1=ftmp
            latest=x1
        else:
            return tmp,0
    return latest,0

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
def f(x):
    return x**3+1
def show():
    plt.subplot(1,2,1)
    x=np.linspace(-10,10,10000)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("secante")
    plt.plot(x,f(x))
    secante(f,-10,10,10e-4)
    plt.subplot(1,2,2)
    x=np.linspace(-10,10,10000)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("bissection")
    plt.plot(x,f(x))
    bissection(f,-4,7,10e-4)
    plt.show()

