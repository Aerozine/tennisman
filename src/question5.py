import time
import numpy as np
import RechercheRacine as ssqrt
import Traject as shot
import const as cst
from scipy.integrate import solve_ivp
import RechercheAvancee as ads

def meilleur_coup(E,direction_v,direction_w,t):
    position=[-11.89,0,2]
    pourcentage=0
    h_1,h_2=0,0
    
    while ( pourcentage <= 1 ):
        valeur_v = (2*pourcentage*E/cst.m)**0.5
        valeur_w = (8*(1-pourcentage)*E/(cst.m*(cst.d**2)))**0.5
        v = valeur_v * direction_v
        w=valeur_w * direction_w
        y=np.concatenate((position, v, w))
        h_1=ads.Getciblehauteur(y, t)
        if h_2<h_1:
            h_2=h_1
            meilleur_pourcentage=pourcentage
            pourcentage=pourcentage+0.00001
    return meilleur_pourcentage  

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
   return ssqrt.bissection(tmp,a,60,cst.bistol)
starttime=time.time()
u=meilleur_coup(70.0,[1.0,0.0,0.0],[0.0,1.0,0.0],10.0)  
g=methodemagique(np.array([-11.89,0,2]),np.array([1,0,0]),np.array([0,1,0]),10,70)
print(time.time()-starttime)
print(u)

