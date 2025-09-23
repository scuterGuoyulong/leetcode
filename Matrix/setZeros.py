class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """O(m+n)空间：用列表记录出现了0元素的i和j信息"""
        axis_x=[]
        axis_y=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    axis_x.append(i)
                    axis_y.append(j)
                    # print(i,j)
        axis_x=set(axis_x)
        axis_y=set(axis_y)
        len_x=len(axis_x)
        len_y= len(axis_y)
        for i in range(m):
            for j in range(n):
                if i in axis_x or j in axis_y:
                    matrix[i][j]=0
        return matrix

"""O(m+n)空间"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        fist_row_has_zero=False
        fist_column_has_zero=False

        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            if matrix[i][0]==0:
                fist_column_has_zero=True
                break

        for i in range(n):
            if matrix[0][i]==0:
                fist_row_has_zero=True
                break

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        # 步骤3：根据第一行和第一列的标记，将除第一行、第一列外的元素置零
        # 处理行（从第1行开始）
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # 处理列（从第1列开始）
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if fist_row_has_zero:
            matrix[0]=[0]*n

        if fist_column_has_zero:
            for i in range(m):
                matrix[i][0]=0

        return matrix