import numpy as np
global d,m, rho , cd , w , h0 , g , hf,e 
 #diametredelabale [d] 0,065
d = 0.065
 #massedelaballe [m] 0,058
m = 0.058
 #massevolumiquedelair [rho] 1,2kg/m^3
rho = 1.2
 #Coefficientdetrainé [Cd] 0,65
cd = 0.65
#Coefficientdemagnus [Cm] 1/2+1,96(v/wd)
#vitessederot [w] 0,300rad/s
w = 0
 #Hauteurdefrappe [Hi] 2m 3m
h0= 2
 #hauteur du filet [Hf] 1m 
hf=1 
 #gravitation [g] 9,81 m/s^2
g=9.81 
 #coefficientderestitution [e] 0.5 0.8
e=-0.8
# calcul de constante utile au calcul 
import numpy as np 
Fp = np.array([0,0,-m*g])
c=(rho*np.pi*d**2)/8

def oderhs(t,y):
    p=y[:3]
    v=y[3:6]
    w=y[6:9]
    normw=np.linalg.norm(w)
    normv=np.linalg.norm(v)
    uv=[y[3]/normv,y[4]/normv,y[5]/normv]
    nFd=cd*c*normv**2
    Fd=[-1* nFd*uv[0],-1* nFd*uv[1],-1* nFd*uv[2]]
    cm=1/(2+(1.96*np.linalg.norm(v)/(normw*d)))
    uFm=cm*c*normv**2
    vcross=np.cross(y[6:9]/normw,y[3:6]/normv)
    Fm=uFm*vcross
    a=(Fd+Fp+Fm)/m
    dy=np.zeros(9)
    dy[:3]=y[3:6]
    dy[3:6]=a
    return dy 
def  trajectoireFiletHorizontal(yInit,T):
    precision=0.000001
    H=precision
    rebond=0
    print(T/precision)
    for i in range(int(T/precision)):
        yInit=yInit+precision*oderhs(T,yInit)
        if yInit[2]<=hf and yInit[0]<=0:
            return (0,0,0)
        if yInit[2]<=0 and rebond<1:
            yInit[5]=e*yInit[5]
            rebond=rebond +1
    Y=(yInit[0],yInit[1],yInit[2])
    return Y 
ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00])            
import time
print(0.000001)
start_time= time.time() # definit le temps initial
a=trajectoireFiletHorizontal(ytest,0.8)     
print(time.time()-start_time)
print(a)
