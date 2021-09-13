# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:48:24 2021

@author: Kurniawan
"""
import numpy as np
import pandas as panda
from first import classData

class classMultiply:
    #create Object Data
    objData=classData()
    
    dataCluter=None
    dataScore=None
    dataMultiply=None
    cluster=None
    scalar=None
    
    def __init__(self):
        self.dataCluter=self.objData.readData()
        self.dataScore=self.objData.getArteryScore()
        self.calMultiply()
        self.getCluster()
    
    def callDataset(self):
        return self.dataCluter
    
    def callArteryScore(self):
        return self.dataScore
    
    def callMultiply(self):
        return self.dataMultiply
        
    # def output(self):
    #     print("Data Artery Score \n",self.dataScore,"\n")
    #     print("Data Score * data \n",self.dataMultiply,"\n")
    
    def calMultiply(self):
        [n,m]=self.dataScore.shape
        multi=[]
        for i in range (n):
            multi1=[]
            for j in range (m):
                multi1.append(self.dataCluter[i,j]*
                              self.dataScore[i,j])
            multi.append(multi1)
        multiply=np.array(multi)
        self.dataMultiply=multiply
    
    def calScalar(self):
        [n,m]=self.dataScore.shape
        scalar=[]
        for i in range(n):
            scalar.append(np.sum(self.dataMultiply[i,:]))
        scalar=np.array(scalar)
        self.scalar=scalar
    
    def readExcel(self):
        file=panda.read_excel(open('data.xlsx','rb'))
        df=panda.DataFrame(
            file,columns=(
                ['ID Cluster']))
        dataset=df.values.tolist()
        dataset=np.array(dataset)
        return dataset
    
    def getCluster(self):
        raw=self.readExcel()
        [n,m]=raw.shape
        cluster=[]
        for i in range(n):
            if raw[i]=='cluster_0':
                cluster.append(0)
            else:
                cluster.append(1)
        self.cluster=np.array(cluster)
    
    def getCluster01(self):
        clus=self.cluster
        scalar=self.scalar
        [n]=clus.shape
        clus0=[]
        clus1=[]
        for i in range (n):
            if clus[i]==0:
                clus0.append(scalar[i])
            else:
                clus1.append(scalar[i])
        clus0=np.array(clus0)
        clus1=np.array(clus1)
        return clus0,clus1
    
    def calPRTA(self):
        clus0,clus1=self.getCluster01()
        max0=max(clus0)
        min0=min(clus0)
        max1=max(clus1)
        min1=max(clus1)
        maximal=max([max0,max1])
        minimal=min([min0,min1])
        R=maximal-minimal
        K=2
        I=R/K
        PRTA=maximal-I
        return PRTA
    
    def getGuttmanClass(self):
        scalar=self.scalar
        n=scalar.shape[0]
        clas=[]
        for i in range (n):
            if scalar[i]>self.calPRTA():
                clas.append(1)
            else:
                clas.append(0)
        clas=np.array(clas)
        return clas
        
# objMultiply=classMultiply()
# objMultiply.calScalar()
# objMultiply.getCluster()
# objMultiply.getGuttmanClass()