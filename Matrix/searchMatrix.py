class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """错误的思路，因为这个不满足"""
        """target > matrix[mid_x][mid_y] 时，你认为目标只可能在 (mid_x, mid_y) 到 (right, bottom) 的子区域中，这是错误的
         —— 因为目标可能在中点的右侧上方或中点的下方左侧，这些区域并不在你划定的子区域内。"""
        m=len(matrix)
        n=len(matrix[0])
        if m==n and m==1:
            if target==matrix[0][0]:
                return True

        if target<matrix[0][0] or target>matrix[m-1][n-1]:
            return False

        left=0
        top=0
        right=m-1
        bottom=n-1

        while target>=matrix[left][top] and target<=matrix[right][bottom] and matrix[left][top]<=matrix[right][bottom]:
            if target==matrix[right][bottom] or target==matrix[left][top]:
                return True
            mid_x=(right+left)/2
            mid_y=(top+bottom)/2
            # 最后到搜索的左上角了，前面已经判断过了，没有就是没有
            if mid_y==top and mid_x==left:
                return False
            # 更新搜索矩阵的区域，类似二分
            if target==matrix[mid_x][mid_y]:
                return True
            elif target>matrix[mid_x][mid_y]:
                left=mid_x
                top=mid_y
            else:
                right=mid_x
                bottom=mid_y

            if left==right and top==bottom:
                break

        return False


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        row,col=0,n-1

        while row<=m-1 and col >=0:
            # 第一行的最大值和最后一列的最小值，可以排除一整行或者列
            nums=matrix[row][col]
            if target==nums:
                return True
            elif target>nums:
                row+=1
            else:
                col-=1
        return False
