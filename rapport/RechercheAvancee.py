import numpy as np
import RechercheRacine as ssqrt
import Traject as shot
import const as cst
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
"""
angle, statut = rechercheangle(y0,ciblerebond)
angle, statut = rechercheAngle2(y0,cibleHauteur)
normeVitesse, statut = rechercheVitesse(y0,cibleRebond)
normeVitesse, statut = rechercheVitesse2(y0,cibleHauteur)
hauteur, statut = rechercheHauteur(y0,cibleRebond)
hauteur, statut = rechercheHauteur2(y0,cibleHauteur)
omega, statut = rechercheOmega(y0,cibleRebond)
omega, statut = rechercheOmega2(y0,cibleHauteur) 
"""
def IsOnTheGround(t,y):
    if(t>10e-4):
        return y[2]
    else:
        return 1
def FiletCourbe(t,y):
    yf=y[0]        
    xp = (-9.144,0,9.144)
    yp = (1.07,0.914,1.07)
    cs = CubicSpline(xp,yp,bc_type='natural')
    if(y[0]<10e-6 and  y[2]<cs(yf) ):
        return 0 
    return 1
FiletCourbe.terminal=True
#avec un y t fixe retourne la pos x de l impact
def Getciblerebond(y,t):
    tmp=np.arange(0,t,cst.precision)
    IsOnTheGround= lambda t,y : y[2]
    IsOnTheGround.terminal=True
    return solve_ivp(shot.oderhs,(0,t),y,t_eval=tmp,events=IsOnTheGround).y_events[0][0][0]

# avec un y t fixe retourne la poz a la ligne de fond 
def Getciblehauteur(y,t,bouncing=True ):
    tmp=np.arange(0,t,cst.precision)
    IsOnTheGround.terminal=True
    IsAtTheEnd=lambda t,y : y[0]-11.89
    IsAtTheEnd.terminal=True
    data =solve_ivp(shot.oderhs,(0,t),y,t_eval=tmp,events=(IsOnTheGround,IsAtTheEnd))
    if(bouncing and data.y_events[0].size!=0):
        data.y_events[0][0][5]=data.y_events[0][0][5]*cst.e
        return Getciblehauteur(data.y_events[0][0],t-data.t_events[0][0],bouncing=False )
    if(data.y_events[1].size==0):
        return -1 
    return data.y_events[1][0][2]
#modifie l inclinaison sur l axe XZ
def rotangle(pos,angle):
# ici la composante en y ne joue en rien  elle est prit en entrée pour simplifier les tableau
   pos[3]=np.sin(angle)*pos[3]
   pos[5]=np.cos(angle)*pos[5]
   return pos
#definit la norme du vecteur 
def multinorm(pos,number):
    norm =np.linalg.norm(pos[3:6])
    if norm == 0:
        pos[3:6]=[0,0,0]
        return pos
    unit=pos[3:6]/ norm
    pos[3:6]=unit*number 
    return pos
#definit la norme du vecteur 
def multiomega(pos,number):
    norm = np.linalg.norm(pos[6:])
    if norm == 0:
        pos[:6]=[0,0,0]
        return pos
    unit=pos[6:]/np.linalg.norm(pos[6:])
    pos[6:]=unit*number 
    return pos
#recherche en fonction du parametre hauteurinitiale
def rechercheHauteur(y,cibleRebond):
    tmp=lambda x : Getciblerebond(np.concatenate((y[:2],[x],y[3:9])),100)
    return ssqrt.bissection(tmp,5,10,cst.tol)
def rechercheHauteur2(y,cibleHauteur):
    tmp=lambda x : cibleHauteur - Getciblehauteur(np.concatenate((y[:2],[x],y[3:9])),100)
    return ssqrt.bissection(tmp,1,10,cst.tol)
#recherche en fonction de l angle
def rechercheangle(y0,ciblerebond):
    tmp=lambda x : Getciblerebond(rotangle(y0,x),100)
    return ssqrt.bissection(tmp,0,np.pi/2,cst.tol)
def rechercheAngle2(y0,cibleHauteur):
    tmp=lambda x : cibleHauteur - Getciblehauteur(rotangle(y0,x),100)
    return ssqrt.bissection(tmp,0,np.pi/2,cst.tol)
#recherche en fonction de la norme de omega
def rechercheOmega(y0,cibleRebond):
    tmp=lambda x : Getciblerebond(multiomega(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
def rechercheOmega2(y0,cibleHauteur):
    tmp=lambda x : cibleHauteur - Getciblehauteur(multiomega(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
#recherche en fonction de la norme de vitesse
def rechercheVitesse(y0,cibleRebond):
    tmp=lambda x : Getciblerebond(multinorm(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
def rechercheVitesse2(y0,cibleHauteur):
    tmp=lambda x : cibleHauteur - Getciblehauteur(multinorm(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
ytest=np.array([-1.189e+01,  0.000e+00,  1.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
#print(Getciblehauteur(ytest,0.8,1000,bouncing=True))
#ytest=np.array([-1.189e+01,  0.000e+00,  1.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
#a=rechercheHauteur2(ytest,1)     
#print(a)
"""
ytest=np.array([-1.189e+01,  0.000e+00,  1.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
import time
start_time= time.time() # definit le temps initial
#a=euler(oderhs,[0,0.8],ytest, events=evenement)
print(time.time()-start_time) # affiche le temps d execution de la methode
print(a)

"""
