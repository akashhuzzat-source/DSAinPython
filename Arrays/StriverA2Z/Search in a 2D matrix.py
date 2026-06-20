class Solution:
    def searchMatrix(self, mat, target):
        newmat=[]
        first=0
        for i in range (len(mat)):
            if(mat[i][first]<= target and mat[i][len(mat[0])-1]>= target):
                newmat.append(mat[i])
        for j in range(len(newmat)):
            if target in newmat[j]:
                return True
        return False



     