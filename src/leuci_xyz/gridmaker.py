"""

RSA 25/2/23
This class handles transformations in 3d space from a plabe defined by 3 given points to the origin

"""

import math
from . import vectorthree as v3

class GridMaker(object):
            
    def get_unit_grid(self,width,samples):
        side = int(math.floor(samples/2))
        offset = (samples-1)/2
        gap = width/(samples-1)

        coords = []
        for i in range(samples):
            row = []            
            for j in range(samples):
                row.append(((i-offset)*gap,(j-offset)*gap))
            coords.append(row)        
        return coords
                        



        
                        