"""
RSA 25/2/23

This class handles 3d matrices
"""

import math
import numpy as np

# class interface
from . import vectorthree as v3

class MatrixThree(object):
    def __init__(self, vals = [0.,0.,0.,0.,0.,0.,0.,0.,0.]):                
        self.npy = np.array(vals)        
        self.npy = self.npy.reshape(3, 3)  
                                
    def get_inverse(self):
        ############################### https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html        
        try:
            from numpy.linalg import inv   
            from numpy.linalg import det
            minv = inv(self.npy)
            m3inv = MatrixThree(minv.reshape(9))
            return m3inv
        except:
            print("!!!!!! error", self.get_key(), det(self.npy))
        return None
        ###############################
                
    def get_determinant(self):                
        #################################
        from numpy.linalg import det
        return det(self.npy)
        #################################
                        
    def get_value(self, row, col):                
        return self.npy[row,col]
                                    
    def put_value(self, val, row, col):            
        self.npy[row,col] = val
                
    def multiply(self, col, byRow):
        ###################################### https://numpy.org/doc/stable/reference/generated/numpy.matmul.html        
        if byRow:
            mm= np.matmul(self.npy.transpose(), col.npy)
        else:
            mm= np.matmul(self.npy, col.npy)
                        
        vv = mm.reshape(3)
        #print("ToList", vv.tolist())
        vm3 = v3.VectorThree(vv[0],vv[1],vv[2])
        return vm3
        
    def get_key(self,rnd=-1):        
        if rnd > -1:                        
            return str(self.npy.reshape(9).round(rnd))
        else:
            return str(self.npy.reshape(9))

    
        