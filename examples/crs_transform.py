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
"""
        _map2xyz[Convert.ToInt32(Words["17_MAPC"])] = 0;
        _map2xyz[Convert.ToInt32(Words["18_MAPR"])] = 1;
        _map2xyz[Convert.ToInt32(Words["19_MAPS"])] = 2;

        _map2crs[0] = Convert.ToInt32(Words["17_MAPC"]);
        _map2crs[1] = Convert.ToInt32(Words["18_MAPR"]);
        _map2crs[2] = Convert.ToInt32(Words["19_MAPS"]);

        cell_dims[0] = Convert.ToDouble(Words["11_CELLA_X"]);
        _cellDims[1] = Convert.ToDouble(Words["12_CELLA_Y"]);
        _cellDims[2] = Convert.ToDouble(Words["13_CELLA_Z"]);

        _axisSampling[0] = Convert.ToInt32(Words["08_MX"]);
        _axisSampling[1] = Convert.ToInt32(Words["09_MY"]);
        _axisSampling[2] = Convert.ToInt32(Words["10_MZ"]);

        _crsStart[0] = Convert.ToInt32(Words["05_NXSTART"]);
        _crsStart[1] = Convert.ToInt32(Words["06_NYSTART"]);
        _crsStart[2] = Convert.ToInt32(Words["07_NZSTART"]);

        _dimOrder[0] = Convert.ToInt32(Words["01_NX"]);
        _dimOrder[1] = Convert.ToInt32(Words["02_NY"]);
        _dimOrder[2] = Convert.ToInt32(Words["03_NZ"]);
        """
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
        angles) #nagles
    xyz_vec = v3.VectorThree(1,2,3)
    crs_vec = crs_space.xyz_to_crs(xyz_vec)
    back_vec = crs_space.crs_to_xyz(crs_vec)

    print("From xyz", xyz_vec.get_key())
    print("To crs", crs_vec.get_key())
    print("Back xyz", back_vec.get_key())
    
    
########################################################################            
tranform_and_back()
