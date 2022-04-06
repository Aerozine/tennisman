import numpy as np 
import const as cst
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

