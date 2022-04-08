import time
import numpy as np
import RechercheRacine as ssqrt
import Traject as shot
import const as cst
from scipy.integrate import solve_ivp
import RechercheAvancee as ads

#retourne la valeur de la derive a un instant t en fonction de t+1
def getdh(y,x,E): 
    cv=np.sqrt(2*E/cst.m)*np.sqrt(x/100)
    cw=np.sqrt(2*E/cst.m*cst.d**2)*np.sqrt(1-x/100)
    v0=np.concatenate((y[:3],y[3:6]*cv,y[6:]*cw)) 
    y0=ads.Getciblehauteur(v0,20)
    cv=np.sqrt(2*E/cst.m)*np.sqrt(cst.precision+x/100)
    cw=np.sqrt(2*E/cst.m*cst.d**2)*np.sqrt(1-cst.precision -x/100)
    v1=np.concatenate((y[:3],y[3:6]*cv,y[6:]*cw)) 
    y1=ads.Getciblehauteur(v1,20)
    #permet d eviter la plage de valeur dont le resultat n existe pas
    if(y0==y1):
        return None
    return (y1-y0)/cst.precision

def methodemagique(pos,dirv,dirw,t,E):
   y=np.zeros(9)
   y[:3]=pos
   y[3:6]=dirv
   y[6:]=dirw
   tmp=lambda x : getdh(y,x,E) 
   a=1
   while type(tmp(a))==type(None) or a>100 :
       a+=1
   if(a==100):
       print("error no None")
       return 0
   return ssqrt.bissection(tmp,a,80,cst.bistol)
#methodemagique(np.array([-11.89,0,2]),np.array([1,0,0]),np.array([0,1,0]),10,70)
