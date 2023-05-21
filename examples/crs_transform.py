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
import leuci_xyz.gridmaker as grid

########## INPUTS #################
# for 6eex
dim_order = [53,36,87]
crs_starts = [-1,-9,-14]
axis_sampling = [24,36,64]
cell_dims = [9.21,11.98,22.8]
angles = [90,90,90]
map2crs = [1,0,2]

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
    xyz_vec = v3.VectorThree(1,2,3)
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

    gm = grid.GridMaker()
    u_coords = gm.get_unit_grid(5,6,2)
    spc = sptr.SpaceTransform(v3.VectorThree(1,2,3), v3.VectorThree(1,0,3), v3.VectorThree(1,2,0))
    xyz_coords = spc.convert_coords(u_coords)        
    crs_coords = crs_space.convert_coords_to_crs(xyz_coords)
    crs_coords.print()


    
    
########################################################################            
tranform_and_back()
