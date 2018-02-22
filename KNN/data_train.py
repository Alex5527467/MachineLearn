# -*- coding: utf-8 -*-
from numpy import *
import os
import numpy as np
from rawdata_loading import dataload
import matplotlib
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import neighbors

#from sklearn.neighbors import KDTree 
#定义kNN分类模型
from matplotlib.colors import ListedColormap
model = neighbors.KNeighborsClassifier(n_neighbors=5, n_jobs=1,algorithm="kd_tree") # 分类/"balltree"


dataMat = dataload.returnMat
classLabelVector = dataload.classLabelVector

#特征值归一化
min_max_scaler = preprocessing.MinMaxScaler()  
X_minMax = min_max_scaler.fit_transform(dataMat)

model.fit(X_minMax, classLabelVector)

predict = model.predict([[0.1,0.2]])  
print predict



number = 0
dataList1 = []
dataMat1 = array([])
dataList2 = []
dataMat2 = array([])
dataList3 = []
dataMat3 = array([])
for i in range(0,len(classLabelVector)):
    if classLabelVector[i] == 1:
        datatemp1 = X_minMax[i,:]
        dataList1.append(datatemp1)
        dataMat1 = np.array(dataList1)
    if classLabelVector[i] == 2:
        datatemp2 = X_minMax[i,:]
        dataList2.append(datatemp2)
        dataMat2 = np.array(dataList2)
    if classLabelVector[i] == 3:
        datatemp3 = X_minMax[i,:]
        dataList3.append(datatemp3)
        dataMat3 = np.array(dataList3)

fig = plt.figure()
ax = fig.add_subplot(111)

# Create color maps
h = .02  # step size in the mesh
x_min, x_max = X_minMax[:, 0].min() - .5, X_minMax[:, 0].max() + .5
y_min, y_max = X_minMax[:, 1].min() - .5, X_minMax[:, 1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
cm = plt.cm.RdBu
cmap_light =ListedColormap(['#FFAAAA','#AAFFAA','#AAAAFF'])#给不同区域赋以颜色
#cmap_bold =ListedColormap(['#FF0000','#003300','#0000FF'])#给不同属性的点赋以颜色
if hasattr(model, "decision_function"):
    Z = model.decision_function(np.c_[xx.ravel(), yy.ravel()])
else:
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z =Z.reshape(xx.shape)
#plt.pcolormesh(xx,yy,Z,cmap=cmap_light)
ax.contourf(xx, yy, Z, cmap=cm, alpha=.8)

ax.scatter(dataMat1[:,0],dataMat1[:,1],c='blue',s=25,alpha=0.4)
ax.scatter(dataMat2[:,0],dataMat2[:,1],c='red',s=25,alpha=0.4)
ax.scatter(dataMat3[:,0],dataMat3[:,1],c='yellow',s=25,alpha=0.4)

plt.show()

