class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """错误做法，将能到达的方法步数加一了"""
        # n = len(nums)
        # min_step =1
        # max_right=nums[0]
        # if n<=1:
        #     return 0
        # # if max_right>=n-1:
        # #     return 1
        # for i in range(1,n):
        #     if max_right>=n-1:
        #         return min_step
        #     if i+nums[i]>max_right:
        #         min_step+=1
        #         max_right=max(max_right,max_right+nums)
        # return min_step
        """应该记录到dp[i]所需要的最小步数"""
        n = len(nums)
        min_step =1
        max_right=nums[0]
        sub_max_right=nums[0]
        if n<=1:
            return 0
        for i in range(1,n):
            if i>sub_max_right:
                min_step+=1
                sub_max_right=max_right
            # if max_right>=n-1:
            #     return min_step
            if i+nums[i]>max_right:
                max_right=max(max_right,i+nums[i])
        return min_step