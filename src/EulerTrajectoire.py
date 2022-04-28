import numpy as np
import const as cst
from scipy.integrate import solve_ivp
#pour minimaliser la charge de calcul repetitive on définit une méta-constante
c=(cst.rho*np.pi*cst.d**2)/(8*cst.m)
def oderhs(t,y):
    v = np.array(y[3:6], dtype=cst.dtype)
    w=np.array(y[6:9],dtype=cst.dtype)
    normv=np.linalg.norm(v)
    normw=np.linalg.norm(w)
    if(normw>0 and normv>0 ): 
        cm=1/(2+(1.96*normv)/(normw*cst.d)) 
        Fm=(cm*c*normv**2)*np.cross(w/normw,v/normv) 
    else: 
        Fm=0.0
    if(normv>0):
        Ft=(-1*cst.cd*c*normv**2)*(v/normv)
    else:
        Ft=0
    Fd=np.array([0,0,cst.g])
    a=Fd+Ft+Fm
    alpha=np.zeros(3)
    return np.concatenate((v,a,alpha))

def euler(f,t_span,y,events = None ):
    t=t_span[0]
    step=int(t_span[1]/cst.precision)
    # on alloue un tableau vide que l on remplira au fur et a mesure
    yt=np.empty((step+1,9),dtype=cst.dtype) 
    yt[0][:]=y
    for i in range(step):
        dy=f(t,y)
        y=y+dy*cst.precision
        t=t+cst.precision 
        if events(t,y):
            yt=np.resize(yt,(i+1,9))# on sépare la partie écrite de la partie empty
            break
        yt[i+1][:]=y
    return yt 
def  trajectoirecomplete(yInit,T,bouncing=True):
    pos=euler(oderhs,[0,T],yInit,events=evenement) 
    for i in range(pos.shape[0]):
        if(pos[i][0]*pos[0][0]<0 and pos[i][5]>0 and pos[i][2]>cst.hf  ):
            return(0,0,0)
    if bouncing:
        pos[-1][5]=pos[-1][5]*cst.e
        return np.append(pos,trajectoirecomplete(pos[-1][:],T-(pos.shape[0]-1)*cst.precision,bouncing=False),axis=0)
    return pos 
def  trajectoireFiletHorizontal(yInit,T,bouncing=True):
    pos=euler(oderhs,[0,T],yInit,events=evenement) 
    for i in range(pos.shape[0]):
        # si on n as pas encore passé le filet(la balle est du meme coté que la pos init)
        # et si la posz de la balle est plus petite que le filet et que la balle descend
        # cela ne sert a rien , la balle ne passera pas le filet 
        if(pos[i][0]*pos[0][0]<0 and pos[i][5]>0 and pos[i][2]>cst.hf  ):
            return(0,0,0)
        #dans le cas d un deuxieme rebond,il suffit de repartir de la dernière position et de redéfinir la vitesse verticale comme multiplié par e 
    if bouncing:
        pos[-1][5]=pos[-1][5]*cst.e
        #pos shape donne la taile du tableau or le premier element contient la pos initale donc on a
        return trajectoireFiletHorizontal(pos[-1][:],T-(pos.shape[0]-1)*cst.precision,bouncing=False)
    return tuple(pos[-1][:3]) 
def evenement(t,y):
    return 0>y[2]
evenement.terminal=True
y=np.array([-11.89, 0, 2 , 50, 1, 0,30, 15, 0])
T=np.array([0,1])
print(euler(oderhs,T,y,evenement))
