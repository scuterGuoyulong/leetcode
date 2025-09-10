class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[1]*(n)
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
        return dp[n]