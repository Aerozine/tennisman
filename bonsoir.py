import numpy as np
# on va creer un petit tableau 
bonsoir=np.ndarray([[1,2,3],[4,5,6]])
print(bonsoir)
print(bonsoir.shape)
# 2 , 3
a=bonsoir.shape
u=np.ndarray((3,3,3))
bonsoir.append(u)
print(bonsoir)
