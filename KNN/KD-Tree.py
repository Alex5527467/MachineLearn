# -*- coding: utf-8 -*-
from sklearn.neighbors import KDTree
import numpy as np




#print np.random.seed(0)
X = np.random.random((10, 3))  # 10 points in 3 dimensions
print X
tree = KDTree(X, leaf_size=2)





#dist, ind = tree.query([X[0]], k=3)
#print dist,ind
