#!/usr/bin/python
# -*- coding: utf-8 -*-
from itertools import product

import sys
import os

from numpy import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pydotplus

from sklearn import tree
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier





def dataload():
    fr =open ('lenses.txt', 'r')
    arraylines = fr.readlines()
    number = len(arraylines)
    returnMat = zeros((number,4))
    classLabelVector = []
    index = 0
    for line in arraylines:
        line = line.strip() #用于移除字符串头尾指定的字符（默认为空格）
        listFromLine = line.split('\t')
        if listFromLine[0] == 'young':
            returnMat[index,0]=0
        elif listFromLine[0] == 'pre':
            returnMat[index,0]=0.5
        elif listFromLine[0] == 'presbyopic':
            returnMat[index,0]=1
        if listFromLine[1] == 'myope':
            returnMat[index,1]=0
        elif listFromLine[1] == 'hyper':
            returnMat[index,1]=1
        if listFromLine[2] == 'no':
            returnMat[index,2]=0
        elif listFromLine[2] == 'yes':
            returnMat[index,2]=1
        if listFromLine[3] == 'reduced':
            returnMat[index,3]=0
        elif listFromLine[3] == 'normal':
            returnMat[index,3]=1
        
        #returnMat[index,:] = listFromLine[0:3]
        if listFromLine[-1] == 'no lenses':
            classLabelVector.append(3)
        elif listFromLine[-1] == 'soft':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'hard':
            classLabelVector.append(1)
        index = index + 1
    return returnMat,classLabelVector



X,y = dataload()

print X,y



# 训练模型，限制树的最大深度4
clf = tree.DecisionTreeClassifier(criterion='entropy')
#拟合模型
clf = clf.fit(X, y)



dot_data = tree.export_graphviz(clf, out_file=None)  
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("iris.pdf")
