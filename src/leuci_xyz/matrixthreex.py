"""
RSA 25/2/23

This class handles 3d matrices
"""

import math
import numpy as np

# class interface
from . import vectorthree as v3

class MatrixThreeX(object):
    def __init__(self, vals = [0,0,0,0,0,0,0,0,0]):
        self.matrix = vals
                
    def get_inverse(self):                
        detWhole = self.get_determinant()
        transp = []
        transp.append(self.matrix[0])
        transp.append(self.matrix[3])
        transp.append(self.matrix[6])
        transp.append(self.matrix[1])
        transp.append(self.matrix[4])
        transp.append(self.matrix[7])
        transp.append(self.matrix[2])
        transp.append(self.matrix[5])
        transp.append(self.matrix[8])

        transpose = MatrixThreeX(transp)
        matinverse = MatrixThreeX()
        
        factor = 1;

        for i in range(3):        
            for j in range(3):                            
                detReduced = transpose.get_inner_determinant(i, j)
                #detReduced = self.get_inner_determinant(i, j)
                matinverse.put_value(detReduced * factor / detWhole, i, j)
                factor *= -1
        return matinverse
        
    def get_determinant(self):                
        factor = -1
        det = 0
        for i in range(3):        
            factor = factor * -1
            row_val = self.matrix[3 * i]
            newdet = self.get_inner_determinant(0, i)
            det = det + (factor * row_val * newdet)
        return det
    

    def get_inner_determinant(self, col, row):        
        smallMat = []
        if (col == 0):         
            if (row != 0):
                smallMat.append(self.matrix[1])
                smallMat.append(self.matrix[2])                
            if (row != 1):            
                smallMat.append(self.matrix[4])
                smallMat.append(self.matrix[5])            
            if (row != 2):            
                smallMat.append(self.matrix[7])
                smallMat.append(self.matrix[8])                        
        elif (col == 1):        
            if (row != 0):
                smallMat.append(self.matrix[0])
                smallMat.append(self.matrix[2])            
            if (row != 1):            
                smallMat.append(self.matrix[3])
                smallMat.append(self.matrix[5])            
            if (row != 2):            
                smallMat.append(self.matrix[6])
                smallMat.append(self.matrix[8])                    
        else: #(col == 1)        
            if (row != 0):
                smallMat.append(self.matrix[0])
                smallMat.append(self.matrix[1])            
            if (row != 1):            
                smallMat.append(self.matrix[3])
                smallMat.append(self.matrix[4])            
            if (row != 2):            
                smallMat.append(self.matrix[6])
                smallMat.append(self.matrix[7])                    
        n11 = smallMat[0]
        n12 = smallMat[1]
        n21 = smallMat[2]
        n22 = smallMat[3]
        return n11 * n22 - n12 * n21
        
    
    def get_value(self, row, col):                        
        pos = row * 3 + col
        return self.matrix[pos]
                            
    def put_value(self, val, row, col):    
        pos = row * 3 + col        
        self.matrix[pos] = val
        
    def multiply(self, col, byRow):        
        ######################################
        #So, this is by row not by column, or,,, anyway which is which...
        col0 = col.A
        col1 = col.B
        col2 = col.C
        scaled = v3.VectorThree()

        if byRow:
            poses = [0,1,2,3,4,5,6,7,8]
        else:
            poses = [0,3,6,1,4,7,2,5,8]
        s0 = col0 * self.matrix[poses[0]]
        s1 = col0 * self.matrix[poses[1]]
        s2 = col0 * self.matrix[poses[2]]
        s0 += col1 * self.matrix[poses[3]]
        s1 += col1 * self.matrix[poses[4]]
        s2 += col1 * self.matrix[poses[5]]
        s0 += col2 * self.matrix[poses[6]]
        s1 += col2 * self.matrix[poses[7]]
        s2 += col2 * self.matrix[poses[8]]
        scaled.put_by_idx(0, s0)
        scaled.put_by_idx(1, s1)
        scaled.put_by_idx(2, s2)
        return scaled

    def get_key(self,rnd=-1):
        if rnd > -1:
             return [round(x,rnd) for x in self.matrix]
        else:
            return str(self.matrix)

    
        