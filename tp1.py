#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:52:58 2017

@author: 11710470
"""

# Partie A
from sklearn import *
from numpy import *
from matplotlib.pyplot import *

# Partie B
iris = datasets.load_iris()

print "donnees:", iris.data
print "noms des variables:", iris.feature_names
print "noms des classes:", iris.target_names
for i in range(0, iris.data.size / 4):
    print iris.data[i]
    print iris.target_names[ iris.target[i] ]
print "Moyennes:", iris.data.mean(0)
print "Ecart-type:", iris.data.std(0)
print "min:", iris.data.min(0)
print "max:", iris.data.max(0)

print "nombre de donnees:", iris.data.size
print "nombre de variables:", iris.data.shape[0]
print "nombre de classes:", iris.data.shape[1]

# Partie C
MNIST = datasets.fetch_mldata('MNIST original')
print "matrice des donnees", MNIST.data
print "nombre de donnees:", MNIST.data.size
print "nombre de variables:", MNIST.data.shape[1]

#for i in range(0, MNIST.data.size):
    #print "donnee: ", MNIST.data[i], "classe:", MNIST.target[i]
print "moyenne:", MNIST.data.mean(0)
print "Ecart-type:", MNIST.data.std(0)
print "min:", MNIST.data.min(0)
print "max:", MNIST.data.max(0)
print "nombre de classes", np.unique(MNIST.target).size

# Partie D
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
X, y = make_blobs(n_samples = 1000,
                  n_features = 2,
                  centers = 4
                  )
plt.scatter(X[:,0], X[:,1], c=y)
plt.title('1000 donnees')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.show()

X1, y1 = make_blobs(n_samples = 100, n_features = 2, centers = 2)
plt.scatter(X1[:,0], X1[:,1], c=y1)
plt.title('100 donnees')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.show()

X2, y2 = make_blobs(n_samples = 500, n_features = 2, centers = 3)
plt.scatter(X2[:,0], X2[:,1], c=y2)
plt.title('500 donnees')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.show()

X_concat, y_concat = np.vstack((X1, X2)), np.hstack((y1,y2))
plt.scatter(X_concat[:,0], X_concat[:,1], c=y_concat)
plt.title('donnees concatenees')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-15,15)
plt.ylim(-15,15)
plt.show()




