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
x,y = 2,3
mat2 = d3.Matrix3d(x,y)
mat2.add(0,1,data=1.2)
mat2.add(1,1,data=2.5)
for i in range(x):
    for j in range(y):
        print(mat2.get_as_np()[i,j], "\t|\t",mat2.get_as_vals()[i][j])
        

print("------ 3d -----")
x,y,z = 2,3,2
mat3 = d3.Matrix3d(x,y,depth=z)
mat3.add(0,1,k=1,data=1.2)
mat3.add(1,1,k=0,data=2.5)
mat3.add(1,2,k=1,data=7)
for i in range(x):
    for j in range(y):
        for k in range(z):
            print(mat3.get_as_np()[i,j,k], "\t|\t",mat3.get_as_vals()[i][j][k])

print(type(mat2))
print(type(mat2.get_as_np()))
print(type(mat2.get_as_vals()))
print(type(mat3))
print(type(mat3.get_as_np()))
print(type(mat3.get_as_vals()))

npp = mat3.get_as_np()
np3d = d3.Matrix3d(1,1,1)
np3d.set_from_np(npp)
print(npp)
