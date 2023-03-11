"""
RSA 27/2/23

This will make a grid and transform the points to the space
"""

## Ensure code is importaed in path
from pathlib import Path
CODEDIR = str(Path(__file__).resolve().parent.parent )+ "/src/"
import sys
sys.path.append(CODEDIR)
from pathlib import Path
import leuci_xyz.vectorthree as v3
import leuci_xyz.spacetransform as sptr
import leuci_xyz.gridmaker as grid

########## INPUTS #################
central = v3.VectorThree(1,2,3)
linear = v3.VectorThree(2,2,2)
planar = v3.VectorThree(3,2,3)

########## EXAMPLE #################
def make_grid(central, linear, planar):    
    # Test SpaceTransform goes back and forth
    st = sptr.SpaceTransform(central, linear, planar, log=True)
    gm = grid.GridMaker()
    u_coords = gm.get_unit_grid(5,6)
    xyz_coords = st.convert_coords(u_coords)
    print(xyz_coords[0][0].get_key())
    
    

make_grid(central, linear, planar)
