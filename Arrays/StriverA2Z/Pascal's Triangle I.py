class Solution:
    def pascalTriangleI(self, r, c):
        pascal = [[0 for j in range(31)] for i in range(31)]

        for i in range(31):
            for j in range(i + 1):
                if j == 0 or j == i:
                    pascal[i][j] = 1
                else:
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

        return pascal[r-1][c-1]