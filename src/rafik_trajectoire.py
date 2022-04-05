import numpy as np
import const as cst
from scipy.integrate import solve_ivp
def odhers(t,y):
    #je calcule les normes 
    position=[y[0],y[1],y[2]]
    vitesse_normale=[y[3],y[4],y[5]]
    vitesse_angulaire=[y[6],y[7],y[8]]
    norme_vitesse_normale=np.linalg.norm(vitesse_normale)
    norme_vitesse_angulaire=np.linalg.norm(vitesse_angulaire)
    #je vais écrire les forces mtn 
    force_cm=1/(2+(1.96*norme_vitesse_normale)/(cst.d*norme_vitesse_angulaire))
    force_frottement= -1* cst.Cd/8 * cst.rho * np.pi * cst.d**2 *norme_vitesse_normale**2
    force_magnus=force_cm/8 * cst.rho * np.pi * cst.d**2 *norme_vitesse_normale**2*np.cross(vitesse_angulaire/norme_vitesse_angulaire,vitesse_normale/norme_vitesse_normale)
    force_gravitaty=np.array([0,0,cst.m*cst.g])
    