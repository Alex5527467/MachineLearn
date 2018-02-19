# -*- coding: utf-8 -*-
from numpy import *
import os
import numpy as np
from rawdata_loading import dataload
import matplotlib
import matplotlib.pyplot as plt



dataMat = dataload.returnMat
classLabelVector = dataload.classLabelVector


number = 0
dataList1 = []
dataMat1 = array([])
dataList2 = []
dataMat2 = array([])
dataList3 = []
dataMat3 = array([])
for i in range(0,len(classLabelVector)):
    if classLabelVector[i] == 1:
        datatemp1 = dataMat[i,:]
        dataList1.append(datatemp1)
        dataMat1 = np.array(dataList1)
    if classLabelVector[i] == 2:
        datatemp2 = dataMat[i,:]
        dataList2.append(datatemp2)
        dataMat2 = np.array(dataList2)
    if classLabelVector[i] == 3:
        datatemp3 = dataMat[i,:]
        dataList3.append(datatemp3)
        dataMat3 = np.array(dataList3)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(dataMat1[:,1],dataMat1[:,2],c='blue',s=25,alpha=0.4)
ax.scatter(dataMat2[:,1],dataMat2[:,2],c='red',s=25,alpha=0.4)
ax.scatter(dataMat3[:,1],dataMat3[:,2],c='yellow',s=25,alpha=0.4)
plt.show()

