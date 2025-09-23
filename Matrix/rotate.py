class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 分层加上逐个元素处理
        n = len(matrix)

        edge = (n ) / 2

        for i in range(edge):
            # 上边界
            for j in range(i, n - i-1):
                tmp=matrix[i][j]
                matrix[i][j]=matrix[n-1-j][i]
                matrix[n-1 - j][i]=matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                matrix[j][n-1-i]=tmp

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 旋转等同于转置加上反转每一行
        n = len(matrix)

        edge = (n ) / 2

        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i]=matrix[i][::-1]