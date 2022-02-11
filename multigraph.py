import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib as mpl
from numpy.polynomial import Polynomial as poly 
import scipy

"""
from ing_theme_matplotlib import mpl_style
mpl.rcParams['toolbar'] = 'None'
def plot(dark):
      mpl_style(dark)
ToolBar : None
plot(dark=True)
"""
import mod 
x = np.linspace(-100,100,10000)
    
y = np.zeros_like(x)
coef = [0,5,0,-12,1]
p=poly(coef)
#plt.figure(figsize=(15,10))
plt.plot(x,p(x),'r')
plt.plot(x,np.zeros_like(x),'b')
plt.plot(p.roots(),np.zeros_like(p.roots()),'og')
plt.legend(['polynome','droite','racines'],loc='best')
plt.ylim(-90,90)
plt.xlim(-30,30)
plt.title('polynome second degré')
plt.ylabel('Axe des Y')
plt.xlabel('Axe des X')
#plt.figure()
plt.plot(x,p(x),'r')

plt.show()
