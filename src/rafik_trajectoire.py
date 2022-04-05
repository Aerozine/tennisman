import numpy as np
import const as cst
from scipy.integrate import solve_ivp
def odhers(t,y):
    #je calcule les normes 
    vitesse_normale=[y[3],y[4],y[5]]
    vitesse_angulaire=[y[6],y[7],y[8]]
    norme_vitesse_normale=np.linalg.norm(vitesse_normale)
    norme_vitesse_angulaire=np.linalg.norm(vitesse_angulaire)
    #je vais écrire les forces mtn 
    force_cm=1/(2+(1.96*norme_vitesse_normale)/(cst.d*norme_vitesse_angulaire))
    force_frottement= -1* cst.Cd/8 * cst.rho * np.pi * cst.d**2 *norme_vitesse_normale**2
    force_magnus=force_cm/8 * cst.rho * np.pi * cst.d**2 *norme_vitesse_normale**2*np.cross(vitesse_angulaire/norme_vitesse_angulaire,vitesse_normale/norme_vitesse_normale)
    force_gravitaty=np.array([0,0,cst.m*cst.g])
    #je cacule les accelerations
    a=(force_frottement+force_magnus+force_gravitaty)/cst.m
    a_angulaire=np.zeros(3)
    return np.concatenate((vitesse_normale,a,a_angulaire))
def evenement(t,y):
    return y[2]
def  trajectoireFiletHorizontal(yInit,T):
    tmp=np.linspace(0,T,int(T/cst.precision))
    data=solve_ivp(odhers,[0,T],yInit,t_eval=tmp,events=evenement,rtol=cst.precision,atol=10**(-8))
    pos=data.y
    #si ca rebondi
    if data==1:
        
        