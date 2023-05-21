"""

RSA 25/2/23
This class handles transformations in 3d space from a plabe defined by 3 given points to the origin

"""

import math
from . import vectorthree as v3
from . import matrix3d as d3

class GridMaker(object):
            
    def get_unit_grid(self,width,samples,depth_samples=1):
        side = int(math.floor(samples/2))
        offset = (samples-1)/2
        gap = width/(samples-1)
        # if there is a depth, there will be fewer samples
        if depth_samples > 1:
            return self.get_unit_grid3d(width,samples, depth_samples)
        else:
            mat2 = d3.Matrix3d(samples,samples)
            for i in range(samples):                
                for j in range(samples):
                    tpl = ((i-offset)*gap,(j-offset)*gap,0)
                    mat2.add(i,j,data=tpl)
            return mat2

    def get_unit_grid3d(self,width,samples,depth_samples):        
        offset = (samples-1)/2
        gap = width/(samples-1)
        # if there is a depth, there will be fewer samples        
        depth_offset =(depth_samples-1)/2
        print(samples,samples,depth_samples)

        mat3 = d3.Matrix3d(samples,samples,depth_samples)
        
        for i in range(samples):            
            for j in range(samples):                
                for k in range(depth_samples):
                    tpl = ((i-offset)*gap,(j-offset)*gap,(k-depth_offset)*gap)
                    mat3.add(i,j,k,data=tpl)                            
        return mat3

    
    
                        
                        