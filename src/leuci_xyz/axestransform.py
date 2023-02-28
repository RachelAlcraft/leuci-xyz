"""

RSA 28/2/23
This class handles transformations of a list of values from one fastest-middle-slow to another
eg
1,2,3,4,5,6 -> F,M,S =  3,2,1 -> if pictures as x,y,z

4,5,6
1,2,3

Transform this list so it looks the same, but has been given fastest=Z, M=X,S=Y







"""

class CrsTransform(object):
    def __init__(self, xlen, ylen, zlen, xmap, ymap, zmap, a,b,c,alpha, beta, gamma):
        # PUBLIC INTERFACE
        self.xlen, self.ylen, self.zlen = zlen, ylen, zlen
        self.xmap, self.ymap, self.zmap = xmap, ymap, zmap
        self.a, self.b, self.c = a, b, c
        self.alpha, self.beta, self.gamma = alpha, beta, gamma
        self._create_transformation()

    ########## PUBLIC INTERFACE #############
    def crs_to_xyz(self):
        pass
    def xyz_to_crs(self):
        pass

    ########## PRIVATE INTERFACE #############
    def _create_transformation(self):
        pass

        