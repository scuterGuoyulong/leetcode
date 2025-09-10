class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """自己写的，但是空间On，可以优化"""
        # n=len(nums)
        # if n<=2:
        #     return max(nums)
        # if n==3:
        #     return max(nums[0]+nums[2],nums[1])
        # dp=n*[0]
        # dp[0]=nums[0]
        # dp[1]=max(nums[0],nums[1])
        # dp[2]=max(nums[0]+nums[2],nums[1])
        # for i in range(3,n):
        #     dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        # return dp[-1]
        """空间优化之后，因为状态转移的当前变量只依赖前两个变量"""
        n = len(nums)
        if n<=2:
            return max(nums)
        prev_prev=nums[0]
        prev=max(nums[0],nums[1])
        for i in range(n-2):
            current = max(prev_prev+nums[i],prev)

            prev_prev,prev=prev,current
        return current