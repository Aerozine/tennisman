import numpy as np 
import const as c
from scipy.integrate import solve_ivp
step = 0.01
def euler(t,y,f):
    yt=[y]
    for i in range(int(t/step)):
       dy=f(t,y)
       y=y+dy*t
       yt=np.append(yt,[y],axis=0)
       if(event(i,y)):
           break
    return yt

def oderhs(t,y):
    p=np.array(y[:3])
    v=np.array(y[3:6])
    w=np.array(y[6:9])
    Fm=c.cm*c.c*np.linalg.norm(v)**2*np.cross(v,w)/np.cross(v,w)
    Ft=c.cd*c.c*np.linalg.norm(v)*v
    a=c.Fd+Ft+Fm
    alpha=[0,0,0]
    return np.concatenate((v,a,alpha)) 
def event(t,y):
    print(y)
    return 0<y[2]
event.terminal = True
y=[10,10,10,5,5,5,0,4,3]
#u=solve_ivp(oderhs,[0,10],y,events=event)

