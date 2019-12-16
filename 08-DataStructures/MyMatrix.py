from random import randrange
class matrix():

    @staticmethod
    def create(x,y):
        matrix = []
        value = 0
        for i in range(x):
            # create single row
            row = []
            for j in range(y):
                row.append(value)
            # add row to matrix
            matrix.append(row)
        return matrix
    @staticmethod    
    def create_2(x,y):
        w,h=y,x
        matrix=[[0 for x in range(w)] for y in range(h)]   
        return matrix  
    @staticmethod
    def create_unit(x):
       m=matrix.create(x,x) 
       return m
    @staticmethod
    def fill_random(matrix,m,n):
        l=len(matrix)
        for i in range(l):
            k=len(matrix[i])
            for j in range (k):
                value=randrange(m,n+1)
                matrix[i][j]=value
        return matrix        
    @staticmethod
    def transponse(m):
        for row in m:
            m2=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
        return m2    

    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)

m = matrix.create_2(3,5)
m = matrix.fill_random(m,1,9)
matrix.print(m)
m2=matrix.transponse(m)
matrix.print(m2)
