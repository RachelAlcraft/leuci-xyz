"""

RSA 25/2/23
This class handles transformations in 3d space from a plabe defined by 3 given points to the origin

"""

from . import vectorthree as v3
from . import matrixthree as m3
from . import matrix3d as d3

import math

class CrsTransform(object):
    def __init__(self,  dim_order,
                        crs_starts,
                        axis_sampling,
                        map2crs,
                        cell_dims,
                        angles ):
        
        self.M_PI = 3.14159265358979323846
        
        # PUBLIC INTERFACE
        self.dim_order = dim_order
        self.crs_starts = crs_starts
        self.axis_sampling = axis_sampling        
        self.map2crs = map2crs
        self.cell_dims = cell_dims
        self.angles = angles        
        self.map2xyz = [0,0,0]
        self.map2xyz[self.map2crs[0]] = 0
        self.map2xyz[self.map2crs[1]] = 1
        self.map2xyz[self.map2crs[2]] = 2                                
        self._create_transformation()
        
    ########## PUBLIC INTERFACE #############
    def crs_to_xyz(self, CRS):
        vXYZ = v3.VectorThree()
        #If the axes are all orthogonal            
        if (self.angles[0] == 90 and self.angles[1] == 90 and self.angles[2] == 90):
            for i in range(3):
                startVal = CRS.get_by_idx(self.map2crs[i])
                startVal *= self.cell_dims[i] / self.axis_sampling[i]
                startVal += self.origin.get_by_idx(i)
                vXYZ.put_by_idx(i, startVal)
        else: # they are not orthogonal        
            vCRS = v3.VectorThree()
            for i in range(3):
                startVal = 0
                if (self.map2crs[0] == i):
                    startVal = self.crs_starts[0] + CRS.A
                elif (self.map2crs[1] == i):
                    startVal = self.crs_starts[1] + CRS.B
                else:
                    startVal = self.crs_starts[2] + CRS.C
                vCRS.put_by_idx(i, startVal);
            vCRS.put_by_idx(0, vCRS.get_by_idx(0) / self.axis_sampling[0])
            vCRS.put_by_idx(1, vCRS.get_by_idx(1) / self.axis_sampling[1])
            vCRS.put_by_idx(2, vCRS.get_by_idx(2) / self.axis_sampling[2])
            vXYZ = self.orthoMat.multiply(vCRS, False)        
        return vXYZ
        
    def xyz_to_crs(self, XYZ):                
        vCRS = v3.VectorThree()
        #If the axes are all orthogonal            
        if (self.angles[0] == 90 and self.angles[1] == 90 and self.angles[2]== 90):
            for i in range(3):            
                startVal = XYZ.get_by_idx(i) - self.origin.get_by_idx(i)
                startVal /= self.cell_dims[i] / self.axis_sampling[i]                
                vCRS.put_by_idx(i, startVal)        
        else: #they are not orthogonal        
            vFraction = self.deOrthoMat.multiply(XYZ, False)
            for i in range(3):            
                val = vFraction.get_by_idx(i) * self.axis_sampling[i] - self.crs_starts[self.map2xyz[i]];
                vCRS.put_by_idx(i, val);                    
        c = vCRS.get_by_idx(self.map2crs[0]);
        r = vCRS.get_by_idx(self.map2crs[1]);
        s = vCRS.get_by_idx(self.map2crs[2]);        
        return v3.VectorThree(c,r,s);

    def convert_coords_to_xyz(self,crs_coords):
        coords = []
        for i in range(len(crs_coords)):
            row = []
            for j in range(len(crs_coords[0])):                
                vec = crs_coords[i][j]
                vec_t = self.crs_to_xyz(vec)
                row.append(vec_t)
            coords.append(row)
        return coords
    
    def convert_coords_to_crs(self,xyz_coords):
        a,b,c = xyz_coords.shape()
        m3 = d3.Matrix3d(a,b,c)        
        for i in range(a):
            for j in range(b):
                for k in range(c):                        
                    vec = xyz_coords.get(i,j,k=k)
                    vec_t = self.xyz_to_crs(vec)
                    m3.add(i,j,k=k,data=vec_t)            
        return m3

    ########## PRIVATE INTERFACE #############
    def _make_ortho(self):        
        alpha = self.M_PI / 180 * self.angles[0]
        beta = self.M_PI / 180 * self.angles[1]
        gamma = self.M_PI / 180 * self.angles[2]
        temp = math.sqrt(1 - math.pow(math.cos(alpha), 2) - math.pow(math.cos(beta), 2) - math.pow(math.cos(gamma), 2) + 2 * math.cos(alpha) * math.cos(beta) * math.cos(gamma))
        v00 = self.cell_dims[0]
        v01 = self.cell_dims[1] * math.cos(gamma)
        v02 = self.cell_dims[2] * math.cos(beta)
        v10 = 0
        v11 = self.cell_dims[1] * math.sin(gamma)
        v12 = self.cell_dims[2] * (math.cos(alpha) - math.cos(beta) * math.cos(gamma)) / math.sin(gamma)
        v20 = 0
        v21 = 0
        v22 = self.cell_dims[2] * temp / math.sin(gamma)

        self.orthoMat = m3.MatrixThree([v00,v01,v02,v10,v11,v12,v20,v21,v22])
        #self.orthoMat = m3.MatrixThree([v00,v10,v20,v01,v11,v21,v02,v12,v22])
        #self.orthoMat = m3.MatrixThree()
        #self.orthoMat.put_value(v00, 0, 0)
        #self.orthoMat.put_value(v01, 0, 1)
        #self.orthoMat.put_value(v02, 0, 2)
        #self.orthoMat.put_value(v10, 1, 0)
        #self.orthoMat.put_value(v11, 1, 1)
        #self.orthoMat.put_value(v12, 1, 2)
        #self.orthoMat.put_value(v20, 2, 0)
        #self.orthoMat.put_value(v21, 2, 1)
        #self.orthoMat.put_value(v22, 2, 2)        
        self.deOrthoMat = self.orthoMat.get_inverse()

    def _make_origin(self):        
        oro = v3.VectorThree()
        for i in range(3):        
            startVal = 0;
            if (self.map2crs[0] == i):
                startVal = self.crs_starts[0]
            elif (self.map2crs[1] == i):
                startVal = self.crs_starts[1]
            else:
                startVal = self.crs_starts[2]
            oro.put_by_idx(i, startVal);        
        oro.put_by_idx(0, oro.get_by_idx(0) / self.axis_sampling[0])
        oro.put_by_idx(1, oro.get_by_idx(1) / self.axis_sampling[1])
        oro.put_by_idx(2, oro.get_by_idx(2) / self.axis_sampling[2])
        #self.origin = self.orthoMat.multiply(oro, True)
        self.origin = self.orthoMat.multiply(oro, False)
        
    def _create_transformation(self):        
        self._make_ortho()
        self._make_origin()               
        
        