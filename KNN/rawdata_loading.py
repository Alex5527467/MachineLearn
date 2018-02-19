# -*- coding: utf-8 -*-
from numpy import *

def dataload():
    fr =open ('datingTestSet.txt', 'r')
    arraylines = fr.readlines()
    number = len(arraylines)
    returnMat = zeros((number,2))
    classLabelVector = []
    index = 0
    for line in arraylines:
        line = line.strip() #用于移除字符串头尾指定的字符（默认为空格）
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:2]
        if listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1] == 'didntLike':
            classLabelVector.append(1)
        index = index + 1
    return returnMat,classLabelVector
class dataload():
    returnMat,classLabelVector = dataload()


#returnMat,classLabelVector = dataprocess()
#print len(returnMat),len(classLabelVector)


