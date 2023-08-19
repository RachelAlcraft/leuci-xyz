

import numpy as np

class Matrix3d(object):
    def __init__(self, width,length,depth=1):
        """
        An arbitrary typed 3d object

        Paramaters
        -----------
        width : int
        length : int
        depth : int = 1

        """
        self.matrix = []
        self.width = width
        self.length = length
        self.depth = depth
        for i in range(width):
            row = []
            for j in range(length):
                col = []
                for k in range(depth):
                    col.append(0)
                row.append(col)
            self.matrix.append(row)

    def shape(self):        
        return (self.width,self.length,self.depth)

    def print(self):        
        for i in range(self.depth):                        
            print("------")
            for j in range(self.length):     
                row = []           
                for k in range(self.width):
                    row.append(self.matrix[k][j][i])
                print(row)
    
    def add(self,i,j,k=0,data=0):
        self.matrix[i][j][k] = data
    
    def get(self,i,j,k=0):
        return self.matrix[i][j][k]

    def set_from_np(self,npy):
        self.matrix.clear()
        self.width, self.length, self.depth = npy.shape        
        for i in range(self.width):
            row = []
            for j in range(self.length):
                col = []
                for k in range(self.depth):
                    col.append(npy[i,j,k])
                row.append(col)
            self.matrix.append(row)

    def get_as_np(self,is2d=False):
        np_vals = np.zeros((self.width,self.length,self.depth))
        for i in range(self.depth):                                    
            for j in range(self.length):                     
                for k in range(self.width):
                    np_vals[k,j,i] = self.get(k,j,k=i)
        if is2d:
            return np_vals[:,:,0]
        else:
            return np_vals
        
    def get_as_vals(self):
        return self.matrix
                



        