# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:34:27 2021

@author: Kurniawan
"""
import pandas as panda
import numpy as np
import matplotlib.pyplot as plt
from thirth import classGuttman

class readData:
    data=None
    label=None
    
    def __init__(self):
        self.getGuttman()
        self.getData()
        # self.data=self.getData()
        # self.label=self.getClass()
        # self.printDataset()
    
    def getClass(self):
        file=panda.read_excel(open('data.xlsx','rb'))
        df=panda.DataFrame(
            file,columns=(
                ['ID Cluster']))
        self.label=df
        dataset=df.values.tolist()
        dataset=np.array(dataset)
        n=dataset.shape[0]
        label=[]
        for i in range(n):
            if dataset[i]=='cluster_1':
                label.append(1)
            else:
                label.append(0)
        return np.array(label)
    
    def getGuttman(self):
        obj=classGuttman()
        lframe=panda.DataFrame(obj.clas,columns=['label'])
        self.label=lframe
        return lframe
    
    def getData(self):
        file=panda.read_excel(open('data.xlsx','rb'))
        df=panda.DataFrame(
            file,columns=(
                ['V/C_Ratio','Good_IRI','Moderately_IRI','LightDamage_IRI',\
                 'HeavyDamage_IRI','2/1UD_VehicleType','2/2UD_VehicleType',\
                     '4/2UD_VehicleType','4/2D_VehicleType','6/2D_VehicleType',\
                         'Horizontal_Alignment','Vertical_Alignment',\
                             'Design_Speed','Shoulder']))
        self.data=df
    
    def getDataset(self):
        dataset=self.data
        dataset['label']=self.label
        return dataset
    
    def printDataset(self):
        print ("data :\n",self.data,"\n")
        print ("class/label \n",self.label)
    
    def countClass1(self):
        return sum(self.label)
    
    def countClass0(self):
        return self.label.shape[0]-sum(self.label)
    
    def plot(self):
        fig=plt.figure()
        ax=fig.add_axes([0,0,1,1])
        langs=['class 1','class 0']
        labels=[self.countClass1(),self.countClass0()]
        ax.bar(langs,labels)
        plt.show()
    
    def informationLabel(self):
        df_target=self.data.label
        target_count=df_target.value_counts()
        print(df_target)
        print(target_count['cluster_0'])
        print(target_count['cluster_1'])
        target_count.plot(kind='bar', title='Count (target)')

data=readData()
lbl=data.label
dt=data.data
lframe=panda.DataFrame(lbl,columns=['label'])
# print(data.countClass1())
# print(data.countClass0())
# df=panda.DataFrame(data.label,index=None,columns='cclass')
# data.plot()
# data.informationLabel()


