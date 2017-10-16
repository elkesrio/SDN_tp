#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:46:13 2017

@author: 11710470
"""

# Partie A
print "Partie A"
from numpy import *
from sklearn import preprocessing

#1
X = [[1, -1, 2], [2, 2, 0], [0, 1, -1]]
#2
X_scaled = preprocessing.scale(X)
#3
print np.mean(X_scaled)
print np.var(X_scaled)


#Partie B
from sklearn.preprocessing import MinMaxScaler
print "\nPartie B"
#1
X2 = [[1, -1, 2], [2, 0, 0], [0, 1, -1]]
#2
print "Moyenne sur les variables avant la normalisation"
print np.mean(X2[0])
print np.mean(X2[1])
print np.mean(X2[2])
#3
print "Moyenne sur les variables après la normalisation"
X2_scaled = MinMaxScaler([0,1]).fit_transform(X)
print np.mean(X2_scaled[0])
print np.mean(X2_scaled[1])
print np.mean(X2_scaled[2])