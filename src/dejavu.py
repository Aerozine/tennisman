import numpy as np
from scipy.integrate import solve_ivp

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

#constante d entree
# x y z vx vy vz wx wy wz
y=[-11.89,0,2,50,1,0,30,15,0]
c=(rho*np.pi*d**2)/8*m
if(normw := np.linalg.norm(w)):
    cm=1/(2+1.96/(d*normw))
else:
    cm=0
def euler(t,y):
    #prends les valeurs initiales et joue avec odehrs pour lui calculer la n+1
    #p pour position
    p=np.array(y[:3])
    #v pour la vitesse 
    v=np.array(y[3:6])
    #w pour omega
    w=np.array(y[6:9])
    # cree un tableau qui contient comme premiere composante la v a l instant 0
    vtot=[v]
    #idem position et acceleration
    ptot=[p]
    a=np.array([0,0,0])
    atot=[a]
    for i in range(int(t/step)):
        # a chaque etape ajoute la valeur actuelle au tableau 
        vtot=np.append(vtot,[y[3:6]],axis=0)
        ptot=np.append(ptot,[y[:3]],axis=0)
        # recupere la valeur de l acceleration
        dy=oderhs(t,y)
        # el famoso formule d euler
        y=y+dy*step
        atot=np.append(atot,[a],axis=0)
        #si jamais la balle se prends le sol , on arrete
        if(p[2]<0):
            break
        #quand il fini la boucle ( que la balle touche le sol ou etape max)
        # on return la valeur des tableau tot
    return ptot,vtot,atot
    
def oderhs(t,y):
# donner les acc en fonction des vitesse  
    #parsing y into p , v and w 
    #computation of the stable variable
    # make sure that the server is using >=3.8
    # https://peps.python.org/pep-0572/
    #Fm=cm*c*np.linalg.norm(v)**2*np.cross(v,w)
    p=np.array(y[:3])
    v=np.array(y[3:6])
    w=np.array(y[6:9])
    alpha=np.array([0,0,0])
        #a(v)
    Fm=cm*c*np.linalg.norm(v)**2*np.cross(v,w)/np.cross(v,w) #--#
    Ft=cd*c*np.linalg.norm(v)*v
    a=Fd+Ft
    return np.concatenate((v,a,alpha))  
# Nextstep aka euler w/o loop
# unecesery work to make beautifull graph
poisson,vache,ecrevisse=euler(5,y)
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt 
ax=plt.axes(projection='3d')
x=poisson[:,0]
y=poisson[:,1]
z=poisson[:,2]
ax.plot3D(x,y,z,'red')
'''
x=vache[:,0]
y=vache[:,1]
z=vache[:,2]
ax.plot3D(x,y,z,'blue')
x=ecrevisse[:,0]
y=ecrevisse[:,1]
z=ecrevisse[:,2]
ax.plot3D(x,y,z,'green')

'''
plt.show()
def event(t,y):
    return 0<y[2]
event.terminal = True

print(solve_ivp(oderhs,(0,40),y).y[:][-1])
print(solve_ivp(oderhs,(0,40),y).y.shape)
