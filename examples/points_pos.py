"""
RSA 27/2/23

Just tests making coords from a string
"""

## Ensure code is importaed in path
from pathlib import Path
CODEDIR = str(Path(__file__).resolve().parent.parent )+ "/src/"
import sys
sys.path.append(CODEDIR)
from pathlib import Path
import leuci_xyz.vectorthree as v3
import leuci_xyz.spacetransform as sptr

########## INPUTS #################
centralstr = "(1.1,2, 3)"
linearstr = "( 2,-2.22,2)"
planarstr = "(3 ,2 ,3) "
width=100
samples=5

########## EXAMPLE #################
def make_coords():    
    central = v3.VectorThree().from_coords(centralstr)
    linear = v3.VectorThree().from_coords(linearstr)
    planar = v3.VectorThree().from_coords(planarstr)

    st = sptr.SpaceTransform(central, linear, planar, log=True)

    posC = st.reverse_transformation(central)
    posL = st.reverse_transformation(linear)
    posP = st.reverse_transformation(planar)
    posCp = posC.get_point_pos(samples,width)
    posLp = posL.get_point_pos(samples,width)
    posPp = posP.get_point_pos(samples,width)

    print(centralstr,posCp.get_key())
    print(linearstr,posLp.get_key())
    print(planarstr,posPp.get_key())

    pos_moved = st.navigate(central,"UP",0.01)
    print("Moved from",central.get_key())
    print("Moved to",pos_moved.get_key())
    


    
    

make_coords()
