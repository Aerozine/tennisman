import numpy as np 
import const as c
from scipy.integrate import solve_ivp
etape = 0.0001
def euler(t,y,f,step = etape ):
    yt=np.array([y])
    for i in range(int(t/step)):
       dy=f(t,y)
       y=y+dy*t*step
       yt=np.append(yt,[y],axis=0)
       if(event(i,y)):
           break
    return yt

def oderhs(t,y):

"""    p=np.array(y[:3])
    v=np.array(y[3:6])
    w=np.array(y[6:9])
    normw=np.linalg.norm(w)
    if(not normw):
        cm=1/(2+1.96*np.linalg.norm(v)/(normw*c.d))
        Fm=cm*c.c*(np.linalg.norm(v)**2)*np.cross(w/normw,v/np.linalg.norm(v))
    else:
        Fm=0
    Ft=-c.cd*c.c*np.linalg.norm(v)*v
    a=c.Fd+Ft+Fm
    alpha=[0,0,0]
    return np.concatenate((v,a,alpha)) 
"""
def event(t,y):
    return 0>y[2]
event.terminal = True
def trajectoireFiletHorizontal(yInit,T,bouncing=True):
    traj=euler(T,yInit,oderhs)
    #interpolation
    i=None
    for i in range(len(traj)-1):
        if traj[i,0]*traj[i+1,0]<=0 and traj[i,2]<c.hf:
            return (0,0,0)
        elif traj[i,2]<0 and traj[i,0]<=0 :
            return (0,0,0)
        if traj[i,2]<=0:
            traj[i,2]=-e*tra
    i=len(traj)-1
    print(traj)
    if(bouncing):
        traj[i-1,5]=traj[i-1,5]*-c.e
        return trajectoireFiletHorizontal(traj[i-1,:],T-etape*i,bouncing=False)
    return (traj[i-1,0],traj[i-1,1],traj[i-1,2])
#b=[-1.189e+01, 0.000e+00 ,1.330e+00, 5.000e+01 ,1.000e+00 ,0.000e+00,      3.000e-03 ,1.500e-03, 0.000e+00] 
b=[-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00,
  3.000e-03 , 1.500e-03,  0.000e+00]
#print(trajectoireFiletHorizontal(b,0.8))
#udada=[2.00643436e+01,6.39086300e-01,1.00607581e-04,5.01204071e+01, 1.00240547e+00,3.13472367e+00,3.00000000e-03,1.50000000e-03 , 0.00000000e+00]
#print(euler(10,udada,oderhs).shape)
:q
:q
