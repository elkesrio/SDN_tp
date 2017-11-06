#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:19:43 2017

@author: 11710470
"""

# E(x) = x4 - 11x3 + 41x2 - 61x + 30

from math import *

def E(x):
    return (x-1)*(x-2)*(x-3)*(x-5)

def deriv_E(x):
    return 4*math.pow(x, 3) - 33*math.pow(x,2) + 82*x -61

# l'algorithme DG
def DG(x0, eta, eps = 0.01, nb_max = 1000):    

    xi = x0
    yi = E(x0)
    plt.scatter(x0, E(x0))
    
    cond = 50000
    nb_iter = 0 
    tmp_y = E(x0)
    while cond > eps and nb_iter < nb_max_iter:
        cond = abs( -eta * deriv_E(xi) )
        # to do ...
        yi = xi - eta * deriv_E(xi)
        # xi = xi - eta * deriv_E(xi)
        yi = E(xi)
        nb_iter = nb_iter + 1
        tmp_y = y0
        plt.scatter(xi, yi)
    
    plt.title("x0 = " + repr(x0) + " eta = " + repr(eta) )
    plt.grid()
    
    plt.savefig("gradient_descent_1d_python.png", bbox_inches='tight')
    plt.show()
    
DG(5, 0.001)
DG(5, 0.01)
DG(5, 0.1)
DG(5, 0.17)
DG(5, 1)
DG(0, 0.001)