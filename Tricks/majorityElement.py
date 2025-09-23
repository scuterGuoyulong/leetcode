class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans =nums[0]
        count=1
        n=len(nums)
        if n==1:
            return ans
        for i in range(1,n):
            if count==0:
                ans=nums[i]
                # count=1
            if nums[i]==ans:
                count+=1
                if count>n/2:
                    return ans
            else:
                count-=1
            print(count)
        return ans