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
import leuci_xyz.matrixthree as m3
import leuci_xyz.matrixthreex as m3x
import leuci_xyz.matrixthreey as m3y


########## INPUTS #################
a = v3.VectorThree(1,2,3)
b = v3.VectorThree(2,-2,2)
c = v3.VectorThree(3,2,0.25)
ver = 0 #0,1 or 2
vals = [1,2,3,4,5,6,7,8,19]
########## EXAMPLE #################
def mat_mult():    
    print("Multiplying vectors...")    
    # Test Vector Mult
    c_l = v3.v3_multiply(a,b).get_key()
    print(c_l, "= (2,-4,6)")
    l_p = v3.v3_multiply(b,c).get_key()
    print(l_p, "= (6,-4,0.5)")

    if ver == 0:
        matm = m3.MatrixThree(vals)
        print("New ver",matm.get_key())
    elif ver == 1:
        matm = m3x.MatrixThreeX(vals)
        print("Parallel ver",matm.get_key())
    elif ver == 2:
        matm = m3y.MatrixThreeY(vals)
        print("Old ver",matm.get_key())

    print("Multiplying matrix to vectors...")    
    m_a = matm.multiply(a,False)
    print(m_a.get_key(),"=(14,32,80) bycol")
    m_b = matm.multiply(b,True)
    print(m_b.get_key(),"=(8,10,32) byrow")

    print("Matrix things...")
    dt = matm.get_determinant()
    print("determinant = -30",dt)
    invm = matm.get_inverse()
    print(invm.get_key(rnd=2))
    print("[-1.56, 0.47, 0.1, 1.13, 0.07, -0.2, 0.1, -0.2, 0.1]")

    print("and reverse...")
    dt = invm.get_determinant()
    print("inv determinant = -0.033",dt)

    invm_back = invm.get_inverse()
    print(invm_back.get_key(rnd=2))

    
    


    
        

mat_mult()
