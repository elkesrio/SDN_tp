#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:46:13 2017

@author: 11710470
"""

# Partie A
print "Partie A"
from sklearn import preprocessing
from sklearn import *
from numpy import *
from matplotlib.pyplot import *
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
#1
X = np.array([[1, -1, 2], [2, 2, 0], [0, 1, -1]])
#2
X_scaled = preprocessing.scale(X)
#3
print np.mean(X_scaled)
print np.var(X_scaled)


#Partie B
from sklearn.preprocessing import MinMaxScaler
print "\nPartie B"
#1
X2 = np.array([[1, -1, 2], [2, 0, 0], [0, 1, -1]])
#2
print "Moyenne sur les variables avant la normalisation"
print np.mean(X2[:,0])
print np.mean(X2[:,1])
print np.mean(X2[:,2])
#3
print "Moyenne sur les variables après la normalisation"
X2_scaled = MinMaxScaler([0,1]).fit_transform(X)
print np.mean(X2_scaled[:,0])
print np.mean(X2_scaled[:,1])
print np.mean(X2_scaled[:,2])

#Partie C
print "\nPartie C"
#1
iris = datasets.load_iris()
#2
print iris.data
X = iris.data  
y = iris.target


plt.figure(2, figsize=(8, 6))
plt.clf()

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('Longeur')
plt.ylabel('Largeur')

plt.xticks(())
plt.yticks(())

plt.show()

print ("La meilleure combinaison qu on a pu remarqué est la combinaison 0,1")
#print(scaler.X2_max_)

#Partie D
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn.lda import LDA 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

pca = decomposition.PCA(n_components=3)
IrisPCA = pca.fit(iris.data).transform(iris.data)

lda = LinearDiscriminantAnalysis(n_components=2)
IrisLDA = lda.fit(iris.data, iris.target).transform(iris.data)

colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(IrisPCA[y == i, 0], IrisPCA[y == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('PCA')

plt.figure()
for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(IrisLDA[y == i, 0], IrisLDA[y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA')

plt.show()