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
import leuci_xyz.matrix3d as d3


print("------ 2d -----")
mat2 = d3.Matrix3d(2,3)
mat2.print()
mat2.add(0,0,data="me")
print(mat2.get(0,0))
mat2.print()
print(mat2.shape())

print("------ 3d -----")
mat3 = d3.Matrix3d(2,3,2)
mat3.print()
mat3.add(0,0,k=0,data="me")
mat3.print()
print(mat3.shape())