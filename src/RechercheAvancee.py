import numpy as np
import RechercheRacine as ssqrt
import Trajectron as shot
import const as cst
from scipy.integrate import solve_ivp
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
#avec un y t fixe retourne la pos x de l impact
def Getciblerebond(y,t):
    tmp=np.arange(0,t,cst.precision)
    IsOnTheGround= lambda t,y : y[2]
    IsOnTheGround.terminal=True
    return solve_ivp(shot.oderhs,(0,t),y,t_eval=tmp,events=IsOnTheGround).y_events[0][0][0]

# avec un y t fixe retourne la poz a la ligne de fond 
def Getciblehauteur(y,t,bouncing=True ):
    tmp=np.arange(0,t,cst.precision)
    IsOnTheGround= lambda t,y : y[2]
    IsOnTheGround.terminal=True
    IsAtTheEnd=lambda t,y : 11.89-y[0]
    IsAtTheEnd.terminal=True
    data =solve_ivp(shot.oderhs,(0,t),y,t_eval=tmp,events=(IsOnTheGround,IsAtTheEnd))
    if(bouncing and data.y_events[0].size!=0):
        print("il y a un rebond en ", data.y_events[0][0][:3])
        data.y_events[0][0][5]=data.y_events[0][0][5]*cst.e
        return Getciblehauteur(data.y_events[0][0],t-data.t_events[0][0],h,bouncing=False )
    return data.y_events[1][0]

#modifie l inclinaison sur l axe XZ
def rotangle(pos,angle):
# ici la composante en y ne joue en rien  elle est prit en entrée pour simplifier les tableau
   pos[3]=np.sin(angle)*pos[3]
   pos[5]=np.cos(angle)*pos[5]
   return pos
#definit la norme du vecteur 
def multinorm(pos,number):
    norm =np.norm(pos[3:6])
    if norm == 0:
        pos[3:6]=[0,0,0]
        return pos
    unit=pos[3:6]/ norm
    pos[3:6]=unit*number 
    return pos
#definit la norme du vecteur 
def multiomega(pos,number):
    norm = np.norm(pos[6:])
    if norm == 0:
        pos[:6]=[0,0,0]
        return pos
    unit=pos[6:]/np.norm(pos[6:])
    pos[6:]=unit*number 
    return pos
#recherche en fonction du parametre hauteurinitiale
def rechercheHauteur(y,cibleRebond):
    tmp=lambda x : Getciblerebond(np.concatenate((y[:2],[x],y[3:9])),100)
    return ssqrt.bissection(tmp,2,3,cst.tol)
def rechercheHauteur2(y,cibleHauteur):
    tmp=lambda x = Getciblehauteur(np.concatenate(((y[:2],[x],y[3:9])),100)
    return ssqrt.bissection(tmp,2,3,cst.tol)
#recherche en fonction de l angle
def rechercheangle(y0,ciblerebond):
    tmp=lambda x : Getciblerebond(rotangle(y0,x),100)
    return ssqrt.bissection(tmp,0,np.pi/2,cst.tol)
def rechercheAngle2(y0,cibleHauteur):
    tmp=lambda x = Getciblehauteur(rotangle(y0,x),100)
    return ssqrt.bissection(tmp,0,np.pi/2,cst.tol)
#recherche en fonction de la norme de omega
def rechercheOmega(y0,cibleRebond):
    tmp=lambda x : Getciblerebond(multiomega(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
def rechercheOmega2(y0,cibleHauteur):
    tmp=lambda x = Getciblehauteur(multiomega(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
#recherche en fonction de la norme de vitesse
def rechercheVitesse(y0,cibleRebond):
    tmp=lambda x : Getciblerebond(multinorm(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
def rechercheVitesse2(y0,cibleHauteur):
    tmp=lambda x = Getciblehauteur(multinorm(y0,x),100)
    return ssqrt.bissection(tmp,0,50,cst.tol)
#ytest=np.array([-1.189e+01,  0.000e+00,  1.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
#print(Getciblehauteur(ytest,0.8,1000,bouncing=True))
"""
ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
import time
start_time= time.time() # definit le temps initial
#a=euler(oderhs,[0,0.8],ytest, events=evenement)
a=rechercheHauteur(ytest,8)     
print(time.time()-start_time) # affiche le temps d execution de la methode
print(a)

"""
