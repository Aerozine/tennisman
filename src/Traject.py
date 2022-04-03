import numpy as np
import const as cst
from scipy.integrate import solve_ivp
#pour minimaliser la charge de calcul repetitive 
# on va sortir de la fonction et les declarer en global les deux trois constantes variables
c=(cst.rho*np.pi*cst.d**2)/(8*cst.m)

def oderhs(t,y):
    print("bonjour")
    p=np.array(y[:3],dtype=cst.dtype)
    v=np.array(y[3:6],dtype=cst.dtype)
    w=np.array(y[6:9],dtype=cst.dtype)
    normv=np.linalg.norm(v)
    if(normw :=np.linalg.norm(w)):
       cm=1/(2+(1.96*normv)/(normw*cst.d)) 
       Fm=(cm*c*normv**2)*np.cross(w/normw,v/normv) 
    else: 
       Fm=np.array([0,0,0],cst.dtype)
    Ft=(-1*cst.cd*c*normv**2)*(v/normv)
    Fd=np.array([0,0,cst.g])
    a=Fd+Ft+Fm
    alpha=np.zeros(3)
    return np.concatenate((v,a,alpha))

def  trajectoireFiletHorizontal(yInit,T,bouncing=True):
   # if method == euler : 
    #freq=1/cst.precision
    tmp=np.linspace(0,T,int(T/cst.precision))
    data=solve_ivp(oderhs,[0,T],yInit,t_eval=tmp,events=evenement,vectorized=False)#,rtol=cst.precision,atol=cst.precision**0.01)
    pos=data.y
    #pos=method(oderhs,[0,T],yInit,events=evenement) 
    for i in range(pos.shape[1]):
        # si on n as pas encore passé le filet(la balle est du meme coté que la pos init)
        # si la posz de la balle est plus petite que le filet et que la balle descend
        # cela ne sert a rien , la balle ne passera pas le filet 
        if( pos[0][i]*pos[0][0]<0 and pos[5][i]>0 and pos[2][i]>cst.hf  ):
            return(0,0,0)
    #dans le cas d un deuxieme rebond il suffit de repartir de la derniere position et de redefinir la vitesse verticale comme multiplié par e 
    if( bouncing ):
        pos[-1][5]=pos[-1][5]*cst.e
        # pos shape donne la taile du tableau or le premier element contient la pos initale
        return trajectoireFiletHorizontal(pos[-1][:],T-(pos.shape[0]-1)*cst.precision,bouncing=False)
    return tuple(pos[-1][:3]) 

def evenement(t,y):
    return y[2]
evenement.terminal=True
ytest=np.array([-1.189e+01,  0.000e+00,  2.000e+00 , 5.000e+01,  1.000e+00 , 0.000e+00, 3.000e-03 , 1.500e-03,  0.000e+00],dtype=cst.dtype)            
#import time
#print(cst.precision)
#start_time= time.time() # definit le temps initial
#a=euler(oderhs,[0,0.8],ytest, events=evenement)
a=trajectoireFiletHorizontal(ytest,0.8)     
#print(time.time()-start_time) # affiche le temps d execution de la methode
print(a)

