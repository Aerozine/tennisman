global d,m, rho , cd , w , h0 , g , hf,e , precision , tol , bistol , atol , rtol
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
#parametre pouvant modifier le type de donnee, la valeur par defaut convient au cas aborde
#si tableau numpy:
#import numpy as np
dtype=None
precision=  0.0001
tol =       0.000001
bistol=     0.000001
rtol=  0.0001
atol=  0.000001
