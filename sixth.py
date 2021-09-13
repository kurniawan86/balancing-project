# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:45:14 2021

@author: Siti Agustini
"""

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import svm

class classifier:
    
    def __init__(self):
        pass
    
    def logicticRegression(self,X,y):
        return LogisticRegression(random_state=0).fit(X,y)
    
    def pickClassifier(self,model,X,y):
        if model=='LogisticRegression':
            return self.logicticRegression(X,y)
        elif model=='SVM':
            return self.svm(X,y)
        elif model=='KNN':
            return self.KNN(X, y)
        elif model=='MLP':
            return self.MLP(X,y)
        else:
            return 0
            
    def svm(self,X,y):
        clf = svm.SVC(kernel='linear', C=2, random_state=42)
        clf.fit(X,y)
        return clf
    
    def MLP(self,X,y):
        clf = MLPClassifier(random_state=1, max_iter=500)
        clf.fit(X,y)
        return clf
    
    def KNN(self,X,y):
        neigh = KNeighborsClassifier(n_neighbors=3)
        neigh.fit(X, y)
        return neigh