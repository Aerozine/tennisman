import numpy as np
import darktheme
########################################
# diametre de la balle
global d
d = 0.065
#masse de la balle
global m 
m = 0.058
#masse volumique de l air
global rho
rho = 1.2
#Coefficient de trainee
global cd
cd = 0.65
#Coefficient de Magnus

#vitesse de rotation
global w 
w = 0
#Hauteur de frappe
global h0
h0 = 2
#Hauteur du filet

#gravitation
global g
g = -9.81
#coefficient de resititution
##############
#bordel 
step=0.01
########################################
#constante pour alleger la charge de calcul 
global Fd 
Fd = np.array([0,0,g])

########################################
#constante d entree
# x y z vx vy vz wx wy wz
y=[10,10,10,5,5,5,0,4,3]
def oderhs(t,y):
    #parsing y 
    p=np.array(y[:3])
    v=np.array(y[3:6])
    w=np.array(y[6:9])
    vtot=[v]
    ptot=[p]
    atot=[[0,0,0]]
    #calcul des constantes dans l acceleration
    c=(rho*np.pi*d**2)/8*m
    # make sure that the server is using >=3.8
    # https://peps.python.org/pep-0572/
    if(normw := np.linalg.norm(w)):
        cm=1/(2+1.96/(d*normw))
    #Fm=cm*c*np.linalg.norm(v)**2*np.cross(v,w)
    else:
        cm=0
    for i in range(int(t/step)):
        Fm=cm*c*np.linalg.norm(v)**2*np.cross(v,w) #--#
        Ft=cd*c*np.linalg.norm(v)*v
        a=Fd+Ft
        print(a) 
        v=nextstep(v,a,step)        
        vtot=np.append(vtot,[v],axis=0)
        p=nextstep(p,v,step)
        ptot=np.append(ptot,[p],axis=0)
        atot=np.append(atot,[a],axis=0)
        if(p[2]<0):
            break
    print("subtest")
    print(vtot,vtot.shape)
    print("subsubtest")
    print(ptot,ptot.shape)
    return ptot,vtot,atot
def nextstep(v,a,step):
    return v+a*step
poisson,vache,ecrevisse=oderhs(10,y)
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 
ax=plt.axes(projection='3d')
x=poisson[:,0]
y=poisson[:,1]
z=poisson[:,2]
ax.plot3D(x,y,z,'red')
x=vache[:,0]
y=vache[:,1]
z=vache[:,2]
ax.plot3D(x,y,z,'blue')
x=ecrevisse[:,0]
y=ecrevisse[:,1]
z=ecrevisse[:,2]
ax.plot3D(x,y,z,'green')


plt.show()
