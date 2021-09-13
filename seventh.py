# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 04:10:16 2021

@author: Siti Agustini
"""
import pandas as panda
from fifth import balancing
from sixth import classifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

class result:
    balance=balancing()
    classy=classifier()
    model=None
    dataset=None
    datasetOri=None
    data=None
    label=None
    X_train=None
    X_test=None
    y_train=None
    y_test=None
    ypred=None
    
    def __init__(self,modelBalancing,model):
        self.datasetOri=self.balance.dfTrain
        if modelBalancing=='none':
            self.dataset=self.balance.dfTrain
            dff=self.dataset["label"]
            print("=====  Original Dataset  =====")
            print("sampling: \n",dff.value_counts())
            dff.value_counts().plot(kind='bar',
                                title='Count (undersampling target)')
            print("======================")
        else:
            self.dataset=self.getBalancingModel(
                modelBalancing)
        self.setTrainTestData()
        print("model balancing data :",modelBalancing)
        self.splitData()
        self.model=self.getModelClassifier(model)
        print("model classifier :",model)
        print("*************************")
        self.scoreTraining()
        self.scoreTest()
        self.writeExcelExixting(modelBalancing,model)
        
    def scoreTraining(self):
        # print("hasil Y prediksi :\n",self.model.predict(self.X_test))
        print("*******************************")
        print("AKURASI Training",
            self.model.score(self.X_test,self.y_test))
        print("*******************************")
        
    def getBalancingModel(self,modelBalancing):
        return self.balance.pickBalancing(modelBalancing)
        
    
    def setTrainTestData(self):
        label=np.array(self.datasetOri.iloc[:,14:15])
        n,m=label.shape
        lab=[]
        for i in range (n):
            lab.append(label[i][0])
        labe=np.array(lab)
        self.label=labe
        self.data=np.array(self.datasetOri.iloc[:,0:14])
        print("dataaaa ",self.data.shape)
        print("*************************")
    
    def splitData(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.data, self.label, test_size=0.33, random_state=42)
        self.X_train=np.array(X_train)
        self.X_test=X_test
        self.y_train=y_train
        self.y_test=y_test
        
    def getResult(self,modelBalancing,model,X,y):
        datanew=self.getBalancingModel(modelBalancing)
        self.model=self.getModelClassifier(model,X,y)
        self.dataset=datanew
    
    def getModelClassifier(self,model):
        return self.classy.pickClassifier(
            model,self.X_train,self.y_train)
    
    def setLabelClassifier(self):
        return self.model.predict(self.data)
    
    def scoreTest(self):
        print("Scoring Testing:")
        print("----------------------------")
        ypred=self.setLabelClassifier()
        accuracy=accuracy_score(ypred,self.label)
        print('Accuracy: %f' % accuracy)
        precision = precision_score(ypred,self.label)
        print('Precision: %f' % precision)
        # recall: tp / (tp + fn)
        recall = recall_score(ypred,self.label)
        print('Recall: %f' % recall)
        # f1: 2 tp / (2 tp + fp + fn)
        f1 = f1_score(ypred,self.label)
        print('F1 score: %f' % f1)
        print("----------------------------")
        print("*************************")
        self.ypred=ypred
    
    def truefalse(self):
        [n]=self.label.shape
        result=[]
        for i in range (n):
            if self.label[i]==self.ypred[i]:
                result.append('True')
        return np.array(result)
        
    def writeExcelExixting(self,modelBalancing,model):
        df=panda.read_excel('alldata.xlsx')
        # print("pppppp \n",np.c_[self.ypred,self.label])
        df.insert(44,"class "+model,self.ypred)
        # df.insert(45,"true/false ",self.truefalse())
        name="result_"+modelBalancing+"_"+model+".xlsx"
        print("name to excel ",name)
        df.to_excel(name)
        
