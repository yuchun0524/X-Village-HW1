import random

class Matrix: 
    def __init__(self, nrows, ncols):
        self.matrix=[[random.randint(0,9) for i in range(ncols)] for j in range(nrows)]
        for i in range(nrows):
            for j in range(ncols):               
                print(self.matrix[i][j],end=' ')
            print("")
        print("")

    def add(self,m):
        if len(self.matrix)==len(m.matrix) and len(self.matrix[0])==len(m.matrix[0]):
            self.l=[[0 for i in range(ncols)] for j in range(nrows)]
            for i in range(nrows):
                for j in range(ncols):
                    self.l[i][j]=self.matrix[i][j]+m.matrix[i][j]
            return self.l   
        
    def sub(self,m):
        if len(self.matrix)==len(m.matrix) and len(self.matrix[0])==len(m.matrix[0]):
            self.c=[[0 for i in range(ncols)] for j in range(nrows)]
            for i in range(nrows):
                for j in range(ncols):
                    self.c[i][j]=self.matrix[i][j]-m.matrix[i][j]
            return self.c 

    def mul(self,m):
        if len(self.matrix[0])==len(m.matrix): 
            self.d=[[0 for i in range(len(m.matrix[0]))] for j in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(m.matrix[0])):
                    for k in range(len(m.matrix)):
                        self.d[i][j]= self.d[i][j] +self.matrix[i][k] * m.matrix[k][j]
            return self.d 

    def transpose(self):
        try:
            self.e=[list(i) for i in zip(*self.d)]
        except AttributeError:
            pass
        else:
            return self.e
            
    def display(self):
        print('========== A + B ==========')
        try:
            for i in range(nrows):
                for j in range(ncols):
                    print(self.l[i][j],end=" ")
                print("")
        except AttributeError:
            print("Matrixs\' size should be in the same size")                
        print("")
        print('========== A - B ==========')
        try:
            for i in range(nrows):
                for j in range(ncols):
                    print(self.c[i][j],end=" ")
                print("")
        except AttributeError:     
            print("Matrixs\' size should be in the same size")               
        print("")
        print('========== A * B ==========')  
        try:
            for i in range(len(self.d)):
                for j in range(len(self.d[0])):
                    print(self.d[i][j],end=" ")
                print("")
        except AttributeError:
            print("Matrix A\'cols must equal Matrix B\'rows")
        print("")
        print('========== the transpose of A * B ==========')
        try:
            for i in range(len(self.e)):
                for j in range(len(self.e[0])):
                    print(self.e[i][j],end=" ")
                print("")
        except AttributeError:
            print("There is nothing to transpose")
# ----------------------------------------- #
nrows=int(input("Enter A matrix's rows:"))
ncols=int(input("Enter A matrix's cols:"))
print('Matrix A',(nrows,ncols),':') 
A=Matrix(nrows,ncols)
nrows=int(input("Enter B matrix's rows:"))
ncols=int(input("Enter B matrix's cols:"))
print('Matrix B',(nrows,ncols),':') 
B=Matrix(nrows,ncols)
A.add(B)
A.sub(B)
A.mul(B)
A.transpose()
A.display()











