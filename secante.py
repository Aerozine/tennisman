import numpy as np
import matplotlib.pyplot as plt 
def secante(f, x0, x1, tol):
    iteration_max=0
    a=f(x0)
    b=f(x1)
    """Comme formulé dans la question on crée 2 variables, a et b afin d'
    invoquer la fonction le moins possible dans la boucle   
    """
    if abs(a)<tol :
        return x0,0
    # au cas ou le x0 est deja le zéro de la fonction f
    
    while iteration_max<100:
    # lors de ce projet on etudie la trajectoire d'une balle, donc on pense que selon la courbure de la fonction 100 itérations de la boucle devrait etre largement suffisant
    
        if b==a :
            print("il y a une erreur car on ne peut pas diviser par 0 ")
            return 18,1
    # on choisi 18 comme x a retourner si il y a une erreur
        if abs(b)< tol :
            return x1,0
        else:
            x_new=x1-b*(x1-x0)/(b-a)
            x0,x1=x1,x_new
        iteration_max+=1
        a=b
        b=f(x1)
        # Voici la technique qui nous a paru la plus logique pour invoquer la fonction 1 seul fois par boucle
    print("il y a une erreur car la fonction ne converge pas")
    return 18,-1


