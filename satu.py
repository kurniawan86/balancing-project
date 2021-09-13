# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:18:44 2021

@author: Kurniawan
"""
import pandas as panda
import numpy as np


class classData:
    dataset = None

    def __init__(self):
        self.readExcel()

    def readData(self):
        return self.dataset

    # method for readExcel to Numpy Array variable
    def readExcel(self):
        file = panda.read_excel(open('data.xlsx', 'rb'))
        df = panda.DataFrame(
            file, columns=(
                ['V/C_Ratio', 'Good_IRI', 'Moderately_IRI', 'LightDamage_IRI',
                 'HeavyDamage_IRI', '2/1UD_VehicleType', '2/2UD_VehicleType',
                 '4/2UD_VehicleType', '4/2D_VehicleType', '6/2D_VehicleType',
                 'Horizontal_Alignment', 'Vertical_Alignment',
                 'Design_Speed', 'Shoulder']))
        dataset = df.values.tolist()
        dataset = np.array(dataset)
        self.dataset = dataset

    # convert Scoring from attribute V/C
    def scoreVC(self):
        data = self.dataset
        attVC = data[:, 0]
        n = attVC.shape[0]
        con = []
        for i in range(n):
            if attVC[i] < 0.2 and attVC[i] >= 0:
                con.append(1)
            elif attVC[i] < 0.45 and attVC[i] >= 0.2:
                con.append(2)
            elif attVC[i] < 0.70 and attVC[i] >= 0.45:
                con.append(3)
            elif attVC[i] < 0.85 and attVC[i] >= 0.7:
                con.append(4)
            elif attVC[i] >= 0.85:
                con.append(5)
            else:
                con.append(0)
        conv = np.array(con)
        return conv

    # convert scoring from Good_IRI
    def scoreGood_IRI(self):
        data = self.dataset
        att = data[:, 1]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 12:
                con.append(4)
            elif att[i] > 8:
                con.append(3)
            elif att[i] > 4:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # convert scoring from Moderately_IRI
    def scoreModerately_IRI(self):
        data = self.dataset
        att = data[:, 2]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 12:
                con.append(4)
            elif att[i] > 8:
                con.append(3)
            elif att[i] > 4:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # convert scoring from LightDamage_IRI
    def scoreLightDamage_IRI(self):
        data = self.dataset
        att = data[:, 3]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 12:
                con.append(4)
            elif att[i] > 8:
                con.append(3)
            elif att[i] > 4:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # convert scoring from HeavyDamage_IRI
    def scoreHeavyDamage_IRI(self):
        data = self.dataset
        att = data[:, 4]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 12:
                con.append(4)
            elif att[i] > 8:
                con.append(3)
            elif att[i] > 4:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # convert scoring 2/1UD_VehicleType
    def scoreVehicle21UD(self):
        data = self.dataset
        att = data[:, 5]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 0:
                con.append(1)
            else:
                con.append(0)
        conv = np.array(con)
        return conv

    # convert scoring 2/2UD_VehicleType
    def scoreVehicle22UD(self):
        data = self.dataset
        att = data[:, 6]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 0:
                con.append(5)
            else:
                con.append(0)
        conv = np.array(con)
        return conv

    # convert scoring 4/2UD_VehicleType
    def scoreVehicle42UD(self):
        data = self.dataset
        att = data[:, 7]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 0:
                con.append(4)
            else:
                con.append(0)
        conv = np.array(con)
        return conv

    # convert scoring 4/2D_VehicleType
    def scoreVehicle42D(self):
        data = self.dataset
        att = data[:, 8]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 0:
                con.append(3)
            else:
                con.append(0)
        conv = np.array(con)
        return conv

    # convert scoring 6/2D_VehicleType
    def scoreVehicle62D(self):
        data = self.dataset
        att = data[:, 9]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 0:
                con.append(2)
            else:
                con.append(0)
        conv = np.array(con)
        return conv

    # convert scoreing horizontal alignment
    def scoreHorizontalAlignment(self):
        data = self.dataset
        att = data[:, 10]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 3.5:
                con.append(3)
            elif att[i] > 0.25:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # convert scoring horizontal alignment
    def scoreVerticalAlignment(self):
        data = self.dataset
        att = data[:, 11]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 45:
                con.append(3)
            elif att[i] > 5:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # convert scoring Design Speed
    def scoreDesignSpeed(self):
        data = self.dataset
        att = data[:, 12]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] > 100:
                con.append(6)
            elif att[i] > 80:
                con.append(5)
            elif att[i] > 65:
                con.append(4)
            elif att[i] > 60:
                con.append(3)
            elif att[i] > 50:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # convert scoring Shoulder
    def scoreShoulder(self):
        data = self.dataset
        att = data[:, 13]
        n = att.shape[0]
        con = []
        for i in range(n):
            if att[i] < 1:
                con.append(2)
            else:
                con.append(1)
        conv = np.array(con)
        return conv

    # method for grouping array ArteryScore
    def getArteryScore(self):
        dataScore = \
            np.column_stack((
                self.scoreVC(),
                self.scoreGood_IRI(),
                self.scoreModerately_IRI(),
                self.scoreLightDamage_IRI(),
                self.scoreHeavyDamage_IRI(),
                self.scoreVehicle21UD(),
                self.scoreVehicle22UD(),
                self.scoreVehicle42UD(),
                self.scoreVehicle42D(),
                self.scoreVehicle62D(),
                self.scoreHorizontalAlignment(),
                self.scoreVerticalAlignment(),
                self.scoreDesignSpeed(),
                self.scoreShoulder()
            ))
        return dataScore

# objData=classData()
# data=objData.readData()
# arteryScore=(objData.getArteryScoring())
