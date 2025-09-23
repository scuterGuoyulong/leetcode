class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k= k%n
        sub_1=nums[:n-k]
        sub_2=nums[n-k:n]
        nums[:k]=sub_2
        nums[k:n]=sub_1
        return nums