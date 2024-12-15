"""
RSA 25/2/23

This class handles 3d vectors
"""

import math
import numpy as np

# class interface

class VectorThree(object):
    def __init__(self, a=0.,b=0.,c=0.,abc=[0.,0.,0.]):    
        if a != 0 or b != 0 or c!=0:
            self.A = a
            self.B = b
            self.C = c        
            self.Valid = True
            self.npy = np.zeros((3))
            self.npy[0] = a
            self.npy[1] = b
            self.npy[2] = c
        else:
            self.npy = np.array(abc)        
            self.A = self.npy[0]
            self.B = self.npy[1]
            self.C = self.npy[2]



    
    def from_coords(self, coords):    
        coords = coords.strip()
        if coords[0] == "(":
            coords = coords[1:]
        if coords[-1] == ")":
            coords = coords[:-1]
        a,b,c = coords.split(",")
        self.A = float(a)
        self.B = float(b)
        self.C = float(c) 
        self.Valid = True
        self.npy = np.array([self.A,self.B,self.C])
        return VectorThree(abc=self.npy.tolist())
                        
    def make_from_key(self,key):                            
        key = key.Substring(1)
        key = key.Substring(0,key.Length-1)
        sk = key.Split(",")
        self.A = float(sk[0])
        self.B = float(sk[1])
        self.C = float(sk[2])        
        self.npy = np.array([self.A,self.B,self.C])
        self.Valid = True
        
    def get_by_idx(self,idx):    
        return  self.npy[idx]   
        #if idx == 0:
        #    return self.A;
        #elif idx == 1:
        #    return self.B;
        #else:
        #    return self.C;
        
    def put_by_idx(self, idx, val):
        self.npy[idx] = val
        if idx == 0:
            self.A = val            
        elif idx == 1:
            self.B = val
        else:
            self.C = val
        
    def distance(self,ABC):    
        dis = (self.A - ABC.A) * (self.A - ABC.A) + (self.B - ABC.B) * (self.B - ABC.B) + (self.C - ABC.C) * (self.C - ABC.C)
        return math.sqrt(dis)
    
    def magnitude(self):        
        mag = (self.A * self.A) + (self.B * self.B) + (self.C * self.C)
        return math.sqrt(mag)
                                                
    def get_angle(self, ABC):    
        BA = VectorThree(0 - self.A, 0 - self.B, 0 - self.C)
        BC = VectorThree(0 - ABC.A, 0 - ABC.B, 0 - ABC.C);
        dot = BA.dot_product(BC);
        magBA = BA.magnitude();
        magBC = BC.magnitude();
        cosTheta = dot / (magBA * magBC);
        theta = math.acos(cosTheta);
        return theta #in radians
    
    def dot_product(self, ABC):
        px = self.A * ABC.A
        py = self.B * ABC.B
        pz = self.C * ABC.C
        return px + py + pz
    
    def get_key(self,rnd = 4):
        strkey = "(" + str(round(self.A, rnd)) + ","
        strkey += str(round(self.B, rnd)) + ","  
        strkey += str(round(self.C, rnd)) + ")"  
        return strkey
            
    def get_point_pos(self, samples, width):    
        gap = width/(samples-1)                        
        PP = VectorThree(self.A, self.B, self.C)        
        PP.A = PP.A / gap
        PP.B = PP.B / gap
        PP.C = PP.C / gap
        adj = (samples-1)/2#(width / (2 * gap))
        #if (int)(samples % 2) != 0:
        #    adj -= 0.5
        PP.A += adj
        PP.B += adj                
        return PP

# static functions

def v3_add(ABC, PQR):        
    A = ABC.A + PQR.A
    B = ABC.B + PQR.B
    C = ABC.C + PQR.C
    return VectorThree(A,B,C)
    
def v3_subtract(ABC, PQR):        
    A = ABC.A - PQR.A
    B = ABC.B - PQR.B
    C = ABC.C - PQR.C
    return VectorThree(A,B,C)

def v3_divide(ABC, PQR):        
    A = ABC.A / PQR.A
    B = ABC.B / PQR.B
    C = ABC.C / PQR.C
    return VectorThree(A,B,C)

def v3_multiply(ABC, PQR):        
    A = ABC.A * PQR.A
    B = ABC.B * PQR.B
    C = ABC.C * PQR.C
    return VectorThree(A,B,C)
