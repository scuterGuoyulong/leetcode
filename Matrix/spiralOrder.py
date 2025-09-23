class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])

        ans = []

        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:

            # 遍历上边界
            for j in range(left, right + 1):
                ans.append(matrix[top][j])

            top += 1

            # 遍历右边界
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # 遍历下边界
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ans.append(matrix[bottom][j])
                bottom -= 1

            # 遍历左边界
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
