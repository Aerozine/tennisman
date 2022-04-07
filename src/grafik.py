import darktheme 
import numpy as np
import const as cst
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
import Traject as shot
import RechercheAvancee as ads
def evenement(t,y):
    return y[2]
evenement.terminal=True
prec=0.1
ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 2.000e+00,  0.000e+00 , 2.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype) 
x=np.arange(1,20,prec)
y=np.arange(1,20,prec)
a=0
z=np.copy(x)
"""
def printgraph(i):
    tmp=np.arange(0,10,cst.precision)
    pos=solve_ivp(shot.oderhs,(0,10),ads.multinorm(ytest,i),t_eval=tmp,events=evenement,rtol=cst.precision,atol=cst.precision**0.01)
    pos.y[5,-1]=pos.y[5,-1]*cst.e
    pos2=solve_ivp(shot.oderhs,(0,10),pos.y[:,-1],t_eval=tmp,events=evenement,rtol=cst.precision,atol=cst.precision**0.01)
    pos.y=np.concatenate((pos.y,pos2.y),axis=1)
    u=pos.y[0,:]
    v=pos.y[2,:]
    plt.plot(u,v)
for i in x :
    y[a]=ads.Getciblehauteur(ads.multinorm(ytest,i),20)
    #if(ads.Getciblehauteur(ads.multinorm(ytest,i),20)==None):
        #printgraph(i)
        #print("none")
    '''
        tmp=np.arange(0,10,cst.precision)
        pos=solve_ivp(shot.oderhs,(0,10),ads.multinorm(ytest,i),t_eval=tmp,events=evenement,rtol=cst.precision,atol=cst.precision**0.01)
        pos.y[5,-1]=pos.y[5,-1]*cst.e
        pos2=solve_ivp(shot.oderhs,(0,10),pos.y[:,-1],t_eval=tmp,events=evenement,rtol=cst.precision,atol=cst.precision**0.01)
        pos.y=np.concatenate((pos.y,pos2.y),axis=1)
        u=pos.y[0,:]
        v=pos.y[2,:]
        plt.plot(u,v)
        plt.show()
        break
        ''' 
    z[a]=(y[a]-y[a-1])/prec
    a+=1
z[0]=0
#u=pos.y[0,:]
#v=pos.y[2,:]
#plt.plot(u,v)
#plt.show()
"""
#plt.plot(x,y)
#plt.plot(x,z)
#"""
#plt.show()



