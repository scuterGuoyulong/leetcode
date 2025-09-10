class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        ans= [[1],[1,1]]
        for i in  range(numRows-2):
            row=[1]
            n=len(ans[-1])
            nums=ans[-1]

            for j in range(1,n):
                row.append(nums[j-1]+nums[j])
            row.append(1)
            ans.append(row)
        return ans
