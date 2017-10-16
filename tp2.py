#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:46:13 2017

@author: 11710470
"""

# Partie A

from numpy import *
from sklearn import preprocessing

#1
X = [[1, -1, 2], [2, 2, 0], [0, 1, -1]]
#2
X_scaled = preprocessing.scale(X)
#3
print np.mean(X_scaled)
print np.var(X_scaled)