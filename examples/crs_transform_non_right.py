"""
RSA 4/2/23

This loads and examines a map file and it's corresponding cif file given the pdb code
It will automatically check what kind of electron ddensity is available - xray or cryo em
"""

## Ensure code is importaed in path
from pathlib import Path
CODEDIR = str(Path(__file__).resolve().parent.parent )+ "/src/"
import sys
sys.path.append(CODEDIR)
from pathlib import Path
import leuci_xyz.vectorthree as v3
import leuci_xyz.spacetransform as sptr
import leuci_xyz.crstransform as crs

########## INPUTS #################
# for 3u7z
dim_order = [110,70,70]
crs_starts = [0,0,0]
axis_sampling = [70,70,110]
cell_dims = [29.685,30.474,47.156]
angles = [73.13,83.8,89.3]
map2crs = [2,0,1]

########## EXAMPLE #################
def tranform_and_back():
    print("Transforming xys<->crs")                                                        
    crs_space = crs.CrsTransform(
        dim_order, #lengths
        crs_starts, #start
        axis_sampling, #adj
        map2crs, #map axes
        cell_dims,#lengths
        angles  )    #nagles
    xyz_vec = v3.VectorThree(abc=[17.691,47.462,-2.114])
    crs_vec = crs_space.xyz_to_crs(xyz_vec)
    back_vec = crs_space.crs_to_xyz(crs_vec)    
    
    print("From xyz", xyz_vec.get_key(rnd=2))
    print("To crs", crs_vec.get_key(rnd=2))
    print("Back xyz", back_vec.get_key(rnd=2))
    print("--------------")

    crs_vec = v3.VectorThree(1,2,3)
    xyz_vec = crs_space.crs_to_xyz(crs_vec)    
    back_vec = crs_space.xyz_to_crs(xyz_vec)    
    print("From crs", crs_vec.get_key(rnd=2))
    print("To xyz", xyz_vec.get_key(rnd=2))
    print("Back crs", back_vec.get_key(rnd=2))
    
    
########################################################################            
tranform_and_back()
