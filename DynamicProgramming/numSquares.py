import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            max_j=int(math.sqrt(i))
            print(max_j)
            for j in range(1,max_j+1):
                if dp[i-j*j]+1 < dp[i]:
                    dp[i]=dp[i-j*j]+1
        return dp[-1]