import numpy as np
import RechercheRacine as ssqrt
import Trajectron as shot
import const as cst
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
def rechercheHauteur(y,cibleRebond):
    tmp=lambda x :  cibleRebond-shot.trajectoireFiletHorizontal(np.concatenate((y[:2],[x],y[3:9])),30,bouncing=False)[0]
    return ssqrt.bissection(tmp,2,3,cst.tol)
ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
def rechercheHauteur2(y,cibleHauteur):
    tmp=lambda x :  shot.trajectoireFiletHorizontal(np.concatenate((y[:2],[x],y[3:9])),30)[2]
    return ssqrt.bissection(tmp,2,3,cst.tol)


def rotangle(pos,angle):
# ici la composante en y ne joue en rien  elle est prit en entrée pour simplifier les tableau
   pos[3]=np.sin(angle)*pos[3]
   pos[5]=np.cos(angle)*pos[5]
   return pos

def rechercheangle(y0,ciblerebond):
    tmp=lambda x :  shot.trajectoireFiletHorizontal(rotangle(y0,x),30)[2]
    return ssqrt.bissection(tmp,0,np.pi/2,cst.tol)

def rechercheAngle2(y0,cibleHauteur):
    tmp=lambda x :  cibleHauteur-shot.trajectoireFiletHorizontal(rotangle(y0,x),30)[2]
    return ssqrt.bissection(tmp,0,np.pi/2,cst.tol)

def multinorm(pos,number):
    norm =np.norm(pos[3:6])
    if norm == 0:
        pos[3:6]=[0,0,0]
        return pos
    unit=pos[3:6]/ norm
    pos[3:6]=unit*number 
    return pos
def multiomega(pos,number):
    unit=pos[6:]/np.norm(pos[6:])
    pos[6:]=unit*number 
    return pos
def rechercheVitesse(y0,cibleRebond):
    tmp=lambda x :  cibleHauteur-shot.trajectoireFiletHorizontal(multinorm(y0,x),30)[2]
    return ssqrt.bissection(tmp,0,100,cst.tol)
#quelle borne ? 
def rechercheVitesse2(y0,cibleHauteur):
    tmp=lambda x :  cibleHauteur-shot.trajectoireFiletHorizontal(multinorm(y0,x),30)[2]
    return ssqrt.bissection(tmp,0,100,cst.tol)

def rechercheOmega(y0,cibleRebond):
    tmp=lambda x :  cibleHauteur-shot.trajectoireFiletHorizontal(multiomega(y0,x),30)[2]
    return ssqrt.bissection(tmp,0,300,cst.tol)
def rechercheOmega2(y0,cibleHauteur):
    tmp=lambda x :  cibleHauteur-shot.trajectoireFiletHorizontal(multiomega(y0,x),30)[2]
    return ssqrt.bissection(tmp,0,300,cst.tol)

ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
import time
start_time= time.time() # definit le temps initial
#a=euler(oderhs,[0,0.8],ytest, events=evenement)
a=rechercheHauteur(ytest,8)     
print(time.time()-start_time) # affiche le temps d execution de la methode
print(a)


