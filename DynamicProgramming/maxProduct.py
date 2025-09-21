class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp_max=n*[float('-inf')]
        dp_min= n*[float('inf')]
        dp_min[0]= nums[0]
        dp_max[0] = nums[0]
        for i in range(1,n):
            dp_min[i] = min(nums[i],dp_max[i-1]*nums[i],dp_min[i-1]*nums[i])
            dp_max[i] = max(nums[i],dp_max[i-1]*nums[i],dp_min[i-1]*nums[i])
        return max(dp_max)
