import numpy as np
import RechercheRacine as ssqrt
import Traject.py as shot
import const as cst
from scipy.integrate import solve_ivp


def meilleur_coup(E,direction_v,direction_w,t):
    position=[-11.89,0,2]
    pourcentage=0
    tmp=np.arange(0,t,cst.precision)
    
    while (pourcentage=<1) :
        valeur_v = (2*pourcentage*E/cst.m)**0.5
        valeur_w = (8*(1-pourcentage)*E/(cts.m*(cst.d**2)))**0.5
        v=valeur_v * direction_v
        w=valeur_w * direction_w
        y=np.concatenate((position, valeur_v, valeur_w))
        pos=solve_ivp(shot.oderhs,(0,t),y,t_eval=tmp,rtol=cst.precision,atol=cst.precision**0.01)
        data=pos.y
        if(bouncing )