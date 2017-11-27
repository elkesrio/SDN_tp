#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:19:43 2017

@author: 11710470
"""

# E(x) = x4 - 11x3 + 41x2 - 61x + 30

import math
import matplotlib.pyplot as plt
import numpy as np
import decimal 

def E(x):
    return (x-1)*(x-2)*(x-3)*(x-5)

def deriv_E(x):
    x = np.longdouble(x)
    return 4*x**3 - 33*x**2 + 82*x -61


# l'algorithme DG
def DG(x0, eta, eps = 0.01, nb_max_iter = 1000):    
    plt.figure()
    xi = np.longdouble(x0)
    yi = np.longdouble(E(x0))
    plt.scatter(x0, E(x0))
    ymin = yi
    xmin = xi
    
    cond = eps + 20.0
    nb_iter = 0 
    while cond > eps and nb_iter < nb_max_iter:
        xii = np.longdouble(xi - eta * deriv_E(xi) )
        yi = E(xi)
        xmin = min([xmin, xii])
        cond = abs( xii - xi )
        xi = xii
        nb_iter = nb_iter + 1        
        plt.scatter(xi, yi)
    
    plt.title("x0 = " + repr(x0) + " eta = " + repr(eta) )
    plt.grid()
    
    plt.savefig("gradient_descent_1d_python.png", bbox_inches='tight')
    plt.show()
    print "Le minimum trouvé: ", xmin, " E(xmin) = ", E(xmin)
    
DG(5, 0.001)
DG(5, 0.01)                                                    
DG(5, 0.1)
DG(5, 0.17)
DG(5, 1.0)
DG(0, 0.001)