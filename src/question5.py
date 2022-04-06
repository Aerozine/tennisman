import numpy as np
import RechercheRacine as ssqrt
import Traject.py as shot
import const as cst
from scipy.integrate import solve_ivp
import RechercheAvancee as ra


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
        h_1=ra.Getciblehauteur(y, t)
        if h_2<h_1:
            h_2=h_1
            meilleur_pourcentage=pourcentage
            pourcentage=pourcentage+0.00001
    return meilleur_pourcentage  
 




