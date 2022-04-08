import numpy as np
import const as cst
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt
import RechercheAvancee as ads
def evenement(t,y):
    return y[2]
evenement.terminal=True
prec=0.1
ytest=[-11.89,0.0,2.0,50.0,1.0,0.0,30.0,15.0,0.0]
#ytest=np.array([-1.189e+01,  0.000e+00,  2.48 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
x=np.arange(2,70,prec)
y=np.arange(2,70,prec)
z=np.copy(x)
def printgraph(i):
    tmp=np.arange(0,10,cst.precision)
    pos=solve_ivp(shot.oderhs,(0,10),ads.multinorm(ytest,np.linalg.norm(ytest)),t_eval=tmp,events=evenement,rtol=cst.precision,atol=cst.precision**0.01)
    pos.y[5,-1]=pos.y[5,-1]*cst.e
    pos2=solve_ivp(shot.oderhs,(0,10),pos.y[:,-1],t_eval=tmp,events=evenement,rtol=cst.precision,atol=cst.precision**0.01)
    pos.y=np.concatenate((pos.y,pos2.y),axis=1)
    u=pos.y[0,:]
    v=pos.y[2,:]
    plt.plot(u,v)
    plt.axvline(0)
    plt.axvline(11.89)
    #plt.plot(0,11.89)
def bonswar(yo,i):
    E=70
    cv=np.sqrt(2*E/cst.m)*np.sqrt(i/100)
    cw=np.sqrt(2*E/cst.m*cst.d**2)*np.sqrt(1-i/100)
    yo[3]=yo[3]*cv
    yo[4]=yo[4]*cv
    yo[5]=yo[5]*cv
    yo[6]=yo[6]*cw
    yo[7]=yo[7]*cw
    yo[8]=yo[8]*cw
    return yo
#np.concatenate((yo[:3],yo[3:6]*cv,yo[6:]*cw)) 

def show1():
    a=0
    for i in x :
        y[a]=ads.Getciblehauteur(ads.multinorm(ytest,i),20)
        if(y[a]==-1):
            y[a]=None
        z[a]=(y[a]-y[a-1])/prec
        a+=1
    z[0]=0
    plt.plot(x,y)
    plt.plot(x,z)
    plt.show()
    
def show():
    a=0
    ytest[3:6]=ytest[3:6]/np.linalg.norm(ytest[3:6])
    ytest[6:]=ytest[6:]/np.linalg.norm(ytest[6:])
    for i in x :
        y[a]=ads.Getciblehauteur(bonswar(ytest,i),20)
        if(y[a]==-1):
            y[a]=None
        z[a]=(y[a]-y[a-1])/prec
        a+=1
    z[0]=0
    plt.plot(x,y)
    plt.plot(x,z)
    plt.show()
