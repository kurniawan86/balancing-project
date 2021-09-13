# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:19:55 2021

@author: Kurniawan
"""
from second import classMultiply
import pandas as panda

class classGuttman:
    obj=classMultiply()
    clas=[]
    path=None
    
    def __init__(self):
        self.path='data.xlsx'
        self.getDataset()
        self.getArteryScore()
        self.getArteryMuliply()
        self.getScalar()
        self.getLabelKmeans()
        self.getGuttmanClass()
    
    #Get dataset from Excel file 
    def getDataset(self):
        return self.obj.callDataset()
        # print("Data Artery Clustered \n",data,"\n")
    
    #calculate Artery Scoring
    def getArteryScore(self):
        score=self.obj.callArteryScore()
        # print("Data Artery Score \n",score,"\n")
    
    #calculate artery multiply
    def getArteryMuliply(self):
        multi=self.obj.callMultiply()
        # print("Data Artery Mulitply \n",multi,"\n")
    
    def getScalar(self):
        self.obj.calScalar()
        # print("Data Artery Scalar \n",self.obj.scalar,"\n")
        
    #labeling class Guttman
    def getGuttmanClass(self):
        self.clas=self.obj.getGuttmanClass()
        # print("Data Guttman Class Rawan \n",self.clas,"\n")
    
    #labeling from clustering kmeans
    def getLabelKmeans(self):
        # print("cluster kmeans",self.obj.cluster,"\n")
        return self.obj.cluster
        
    #export single value
    def writeExcel(self):
        df = panda.DataFrame(self.clas,
                             columns=['classGutman'])
        df.to_excel("classGutman.xlsx")
    
    #export to exixting value
    def writeExcelExixting(self):
        df=panda.read_excel('data.xlsx')
        df.insert(15,"clsdassGutman",self.clas)
        df.to_excel("dataanyar.xlsx")
    
    def writeExcelAllData(self):
        data=self.obj.callDataset()
        score=self.obj.callArteryScore()
        multi=self.obj.callMultiply()
        df=panda.DataFrame(data=None,index=None)

        #attribute V/C_Ratio
        df.insert(0,"V/C_Ratio",data[:,0])
        df.insert(1,"V/C_Ratio Score",score[:,0])
        df.insert(2,"V/C_Ratio multiply",multi[:,0])
        df.insert(3,"Good_IRI",data[:,1])
        df.insert(4,"Good_IRI Score",score[:,1])
        df.insert(5,"Good_IRI multiply",multi[:,1])
        df.insert(6,"Moderately_IRI",data[:,2])
        df.insert(7,"Moderately_IRI score",score[:,2])
        df.insert(8,"Moderately_IRI multiply",multi[:,2])
        df.insert(9,"LightDamage_IRI",data[:,3])
        df.insert(10,"LightDamage_IRI score",score[:,3])
        df.insert(11,"LightDamage_IRI multiply",multi[:,3])
        df.insert(12,"HeavyDamage_IRI",data[:,4])
        df.insert(13,"HeavyDamage_IRI score",score[:,4])
        df.insert(14,"HeavyDamage_IRI multiply",multi[:,4])
        df.insert(15,"2/1UD_VehicleType",data[:,5])
        df.insert(16,"2/1UD_VehicleType score",score[:,5])
        df.insert(17,"2/1UD_VehicleType multiply",multi[:,5])
        df.insert(18,"2/2UD_VehicleType",data[:,6])
        df.insert(19,"2/2UD_VehicleType score",score[:,6])
        df.insert(20,"2/2UD_VehicleType multiply",multi[:,6])
        df.insert(21,"4/2UD_VehicleType",data[:,7])
        df.insert(22,"4/2UD_VehicleType score",score[:,7])
        df.insert(23,"4/2UD_VehicleType multiply",multi[:,7])
        df.insert(24,"4/2D_VehicleType",data[:,8])
        df.insert(25,"4/2D_VehicleType score",score[:,8])
        df.insert(26,"4/2D_VehicleType multiply",multi[:,8])
        df.insert(27,"6/2D_VehicleType",data[:,9])
        df.insert(28,"6/2D_VehicleType score",score[:,9])
        df.insert(29,"6/2D_VehicleType multiply",multi[:,9])
        df.insert(30,"Horizontal_Alignment",data[:,10])
        df.insert(31,"Horizontal_Alignment score",score[:,10])
        df.insert(32,"Horizontal_Alignment multiply",multi[:,10])
        df.insert(33,"Vertical_Alignment",data[:,11])
        df.insert(34,"Vertical_Alignment score",score[:,11])
        df.insert(35,"Vertical_Alignment multiply",multi[:,11])
        df.insert(36,"Design_Speed",data[:,12])
        df.insert(37,"Design_Speed score",score[:,12])
        df.insert(38,"Design_Speed multiply",multi[:,12])
        df.insert(39,"Shoulder",data[:,13])
        df.insert(40,"Shoulder score",score[:,13])
        df.insert(41,"Shoulder multiply",multi[:,13])
        df.insert(42,"Artery scalar",self.obj.scalar)
        df.insert(43,"Guttman Class",self.clas)
        #save to excel
        df.to_excel("alldata.xlsx",index=False)
        
obj=classGuttman()
obj.writeExcelAllData()


# obj.writeExcel()
# obj.writeExcelExixting()
    