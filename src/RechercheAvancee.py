import numpy as np
import RechercheRacine as ssqrt
import Trajectron as shot
import const as cst
"""
angle, statut = rechercheAngle(y0,cibleRebond)
angle, statut = rechercheAngle2(y0,cibleHauteur)
normeVitesse, statut = rechercheVitesse(y0,cibleRebond)
normeVitesse, statut = rechercheVitesse2(y0,cibleHauteur)
hauteur, statut = rechercheHauteur(y0,cibleRebond)
hauteur, statut = rechercheHauteur2(y0,cibleHauteur)
omega, statut = rechercheOmega(y0,cibleRebond)
omega, statut = rechercheOmega2(y0,cibleHauteur) 
"""
def rechercheHauteur(y,cibleRebond):
    tmp=lambda x :  cibleRebond-shot.trajectoireFiletHorizontal(np.concatenate((y[:2],[x],y[3:9])),30,bouncing=False)[2]
    return ssqrt.bissection(tmp,2,3,cst.tol)
ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
def rechercheHauteur2(y,cibleRebond):
    tmp=lambda x :  shot.trajectoireFiletHorizontal(np.concatenate((y[:2],[x],y[3:9])),30)[2]
    return ssqrt.bissection(tmp,2,3,cst.tol)


def rechercheAngle(y0,cibleRebond):

def rechercheAngle2(y0,cibleHauteur):

def rechercheVitesse(y0,cibleRebond):

def rechercheVitesse2(y0,cibleHauteur):

def rechercheOmega(y0,cibleRebond):

def rechercheOmega2(y0,cibleHauteur) :






ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
import time
start_time= time.time() # definit le temps initial
#a=euler(oderhs,[0,0.8],ytest, events=evenement)
a=rechercheHauteur(ytest,8)     
print(time.time()-start_time) # affiche le temps d execution de la methode
print(a)


