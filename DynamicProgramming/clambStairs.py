class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev_n1=1
        prev_n2=2
        if n==1:
            return 1
        if n==2:
            return 2
        for i in range(n-2):
            prev_n=prev_n1+prev_n2
            prev_n1=prev_n2
            prev_n2=prev_n
        return prev_n
