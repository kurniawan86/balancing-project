# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 09:19:55 2021

@author: Kurniawan
"""
from fourth import readData
import pandas as panda
import numpy
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
from imblearn.under_sampling import NearMiss
from imblearn.under_sampling import CondensedNearestNeighbour

class balancing:
    dfData=readData()
    dfTrain=None
    dfClass0=None
    dfClass1=None
    
    def __init__(self):
        self.concatData()
        self.sampling()
    
    def concatData(self):
        result=panda.concat([self.dfData.data,
                             self.dfData.label],axis=1)
        self.dfTrain=result
    
    def pickBalancing(self,model):
        dataset=None
        if model=='SMOTE':
            dataset=self.SMOTE()
        elif model=='ADASYN':
            dataset=self.ADASYN()
        elif model=='Under Sampling':
            dataset=self.underSampling()
        elif model=='Random Under Sampling':
            dataset=self.randomUnderSampling()
        elif model=='Over Sampling':
            dataset=self.overSampling()
        elif model=='SMOTEENN':
            dataset=self.SMOTEENN()
        elif model=='Near Miss':
            dataset=self.nearMiss()
        return dataset
    
    #resampling
    def sampling(self):
        countClass0,countClass1=self.dfData.label.value_counts()
        dfClass0=self.dfTrain[
            self.dfTrain['label']==0]
        dfClass1=self.dfTrain[
            self.dfTrain['label']==1]
        self.dfClass0=dfClass0
        self.dfClass1=dfClass1
    
    def underSampling(self):
        countClass0,countClass1=self.dfData.label.value_counts()
        dfClass0_under=self.dfClass0.sample(countClass1)
        dfTest_under=panda.concat([dfClass0_under,self.dfClass1]
                                  ,axis=0)
        dff=dfTest_under["label"]
        print("=====  Under Sampling  =====")
        print("random under sampling: \n",
              dff.value_counts())
        dff.value_counts().plot(kind='bar',
                                title='Count (undersampling target)')
        print("======================")
        return dfTest_under
    
    def overSampling(self):
        countClass0,countClass1=self.dfData.label.value_counts()
        dfClass1_over=self.dfClass1.sample(countClass0,replace=True)
        dfTest_over=panda.concat([self.dfClass0,
                                  dfClass1_over],axis=0)
        dff=dfTest_over["label"]
        print("=====  Over Sampling   =====")
        print("random over sampling: \n",
              dff.value_counts())
        dff.value_counts().plot(kind='bar',
                                title='Count (oversampling target)')
        print("======================")
        return dfTest_over
    
    def plot(self,name,target_count):
        print("===== ",name,"   =====")
        print(target_count[0])
        print(target_count[1])
        target_count.plot(kind='bar', title=name)
        print("======================")
        print("")
        
    def SMOTE(self):
        smote=SMOTE()
        data=self.dfData.data
        label=self.dfData.label
        x,y=smote.fit_sample(data,label)
        target_count=y.value_counts()
        # print("=====  SMOTE   =====")
        # print(target_count[0])
        # print(target_count[1])
        # target_count.plot(kind='bar', title='Count (SMOTE target)')
        # print("======================")
        # print("\n\n")
        self.plot('SMOTE',target_count)
        dff=panda.concat([x,y],axis=1)
        return dff
    
    def ADASYN(self):
        ada=ADASYN()
        data=self.dfData.data
        label=self.dfData.label
        x,y=ada.fit_sample(data,label)
        target_count=y.value_counts()
        self.plot('ADASYN',target_count)
        dff=panda.concat([x,y],axis=1)
        return dff
    
    def randomUnderSampling(self):
        rus=RandomUnderSampler()
        data=self.dfData.data
        label=self.dfData.label
        x,y=rus.fit_sample(data,label)
        target_count=y.value_counts()
        self.plot('Random Under Sampling',target_count)
        dff=panda.concat([x,y],axis=1)
        return dff
    
    def SMOTEENN(self):
        smo=SMOTEENN()
        data=self.dfData.data
        label=self.dfData.label
        x,y=smo.fit_sample(data,label)
        target_count=y.value_counts()
        self.plot('SMOTEeNN',target_count)
        dff=panda.concat([x,y],axis=1)
        return dff
    
    def nearMiss(self):
        under=NearMiss()
        data=self.dfData.data
        label=self.dfData.label
        x,y=under.fit_sample(data,label)
        target_count=y.value_counts()
        self.plot('Near Miss',target_count)
        dff=panda.concat([x,y],axis=1)
        return dff

    
# balance=balancing()
# # # # dfUnder=balance.underSampling()
# # # dfOver=balance.overSampling()
# # # dfSmote=balance.SMOTE()
# # # dfAdasyn=balance.ADASYN()
# # # dfRandomUnder=balance.randomUnderSampling()
# # # dfSmooteenn=balance.SMOTEENN()
# sapi=balance.pickBalancing('Over Sampling')
