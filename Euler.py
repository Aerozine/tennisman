import numpy as np 
import const
step = 0.01
def euler(t,y,f)
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
    Fm=cm*c*np.linalg.norm(v)**2*np.cross(v,w)/np.cross(v,w)
    Ft=cd*c*np.linalg.norm(v)*v
    a=Fd+Ft+Fm
    return np.concatenate((v,a,alpa)) 
