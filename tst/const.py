global d,m, rho , cd , w , h0 , g , hf,e , precision , tol
#diametredelabale [d] 0,065
d = 0.065
#massedelaballe [m] 0,058
m = 0.058
#massevolumiquedelair [rho] 1,2kg/m^3
rho = 1.2
#Coefficientdetrainé [Cd] 0,65
cd = 0.65
#Coefficientdemagnus [Cm] 1/2+1,96(v/wd)
#
#vitessederot [w] 0,300rad/s
#w = 0
#Hauteurdefrappe [Hi] 2m 3m
h0= 2
#hauteur du filet [Hf] 1m 
hf=1 
#gravitation [g] 9,81 m/s^2
g=-9.81 
#coefficientderestitution [e] 0.5 0.8
e=-0.7
# size of any ndarray for accuracy and perf
import numpy as np
dtype=np.float32
#pour plus de lenteur et de precision float64  fait le travail , pour l instant c est inutile de l utiliser
precision=0.000001
tol = 0.01
