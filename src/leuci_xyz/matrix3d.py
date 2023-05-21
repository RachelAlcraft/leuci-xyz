



class Matrix3d(object):
    def __init__(self, width,length,depth=1):
        self.matrix = []
        self.width = width
        self.length = length
        self.depth = depth
        for i in range(width):
            row = []
            for j in range(length):
                col = []
                for k in range(depth):
                    col.append(0)
                row.append(col)
            self.matrix.append(row)

    def shape(self):        
        return (self.width,self.length,self.depth)

    def print(self):        
        for i in range(self.depth):                        
            print("------")
            for j in range(self.length):     
                row = []           
                for k in range(self.width):
                    row.append(self.matrix[k][j][i])
                print(row)
    
    def add(self,i,j,k=0,data=0):
        self.matrix[i][j][k] = data
    
    def get(self,i,j,k=0):
        return self.matrix[i][j][k]

        