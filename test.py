import RechercheRacine
import numpy as np
def a(x):
    return np.cos(x)
print(RechercheRacine.bissection(a,1,6,0.0000001))
