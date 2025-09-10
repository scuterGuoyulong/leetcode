class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """前缀和的方式"""
        # n=len(nums)
        # prefix=(n+1)*[0]
        # sum=0
        # # 前缀和
        # for i in range(1,n+1):
        #     sum+=nums[i]
        #     prefix[i]=sum
        #
        # # 统计后方的最大值
        # max_right=(n+1)*[0]
        # max_num=prefix[n]
        # for i in range(n,-1,-1):
        #     if prefix[i]>max_num:
        #         max_num=prefix[i]
        #     max_right[i]=max_num
        #
        # max_sub_sum=prefix[0]
        # for i in range(n+1):
        #     sub_sum=max_right[i]-prefix[i]
        #     if sub_sum>max_sub_sum:
        #         max_sub_sum=sub_sum
        # return max_sub_sum
        n=len(nums)

        dp=n*[0]
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i]=max(nums[i],dp[i-1]+nums[i])
        return max(dp)