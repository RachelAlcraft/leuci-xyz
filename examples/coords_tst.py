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

########## INPUTS #################
centralstr = "(1.1,2, 3)"
linearstr = "( 2,-2.22,2)"
planarstr = "(3 ,2 ,3) "

########## EXAMPLE #################
def make_coords():    
    central = v3.VectorThree().from_coords(centralstr)
    linear = v3.VectorThree().from_coords(linearstr)
    planar = v3.VectorThree().from_coords(planarstr)

    print(centralstr, central.A, central.B, central.C)
    print(linearstr, linear.A, linear.B, linear.C)
    print(planarstr, planar.A, planar.B, planar.C)

    central2 = v3.VectorThree(central.A, central.B, central.C)
    linear2 = v3.VectorThree(linear.A, linear.B, linear.C)
    planar2 = v3.VectorThree(planar.A, planar.B, planar.C)

    print(centralstr, central2.A, central2.B, central2.C)
    print(linearstr, linear2.A, linear2.B, linear2.C)
    print(planarstr, planar2.A, planar2.B, planar2.C)
    

make_coords()
