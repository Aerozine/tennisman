import numpy as np
import const as cst
#pour minimaliser la charge de calcul repetitive 
# on va sortir de la fonction et les declarer en global les deux trois constantes variables
c=(cst.rho*np.pi*cst.d**2)/(8*cst.m)
def oderhs(t,y):
    p=np.array(y[:3],dtype=cst.dtype)
    v=np.array(y[3:6],dtype=cst.dtype)
    w=np.array(y[6:9],dtype=cst.dtype)
    normv=np.linalg.norm(v)
    if(normw :=np.linalg.norm(w)):
       cm=1/(2+(1.96*normv)/(normw*cst.d))
       Fm=(cm*c*normv**2)*np.cross(w/normw,v/normv)
    else:
        Fm=0.0
    Ft=(-1*cst.cd*c*normv**2)*(v/normv)
    Fd=np.array([0,0,cst.g])
    a=Fd+Ft+Fm
    alpha=np.zeros(3)
    return np.concatenate((v,a,alpha))
# fun ,tspan,y0,events steps
def euler(fun, t_span, y0,events=None ):
    data=np.array([0,0,0],dtype=cst.dtype)
    t=t_span[0]
    while(events):
        y0=y0*fun(t,y0)*cst.step
        t=t+cst.step
        data=np.append([data],nd.array(
    return data

def  trajectoireFiletHorizontal(yInit,T,bouncing=True):
    step=int(T/precision))
    array=euler(oderhs,T,yInit)
    for i in range(len(array)):
        if  yInit[2]<=hf and yInit
    precision=0.000001
    H=precision
    rebond=0
    for i in range(int(T/precision)):
        yInit=yInit+precision*oderhs(T,yInit)
        if yInit[2]<=cst.hf and yInit[0]<=0:
            return (0,0,0)
        if yInit[2]<=0 and rebond<1:
            yInit[5]=cst.e*yInit[5]
            rebond=rebond +1
    Y=(yInit[0],yInit[1],yInit[2])
    return Y



 ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00])            
print(euler(oderhs, 


 #import time
#start_time= time.time() # definit le temps initial
 #a=trajectoireFiletHorizontal(ytest,0.8)     
 #print(start_time-time.time())
