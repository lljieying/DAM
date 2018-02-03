import numpy as np
import matplotlib.pyplot as plt
import math

# input: 1) x: the independent variables (data matrix), as a N x M dimensional matrix as a numpy array
#        2) y: the dependent variable, as a N dimensional vector as a numpy array
#
# output: 1) the regression coefficients as a (M+1) dimensional vector as a numpy array
#
# note: the regression coefficients should include the w_0 (the free parameter), thus having dimension (M+1).
# note: The tested datamatrix is **NOT** extended with a column of 1's - if you prefer to do this, then you can do it inside the function by extending x.       
def multivarlinreg(x, y):
    r, c = x.shape
    X = np.c_[ np.ones(r), x] #include column of 1s to data matrix
    print X.shape
    
    w = np.dot( np.dot( ( np.linalg.inv(np.dot(np.transpose(X), X)) ), np.transpose(X) ), y)
    return w
    pass