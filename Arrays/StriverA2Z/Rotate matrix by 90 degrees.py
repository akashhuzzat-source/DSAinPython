class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)
        newnums = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                newnums[j][n-1-i]=matrix[i][j]
        return newnums
    