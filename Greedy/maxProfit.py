class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min=prices[0]
        n=len(prices)
        min_nums=n*[0]
        for i in range(n):
            if prices[i]<min:
                min=prices[i]
            min_nums[i]=min
        for i in range(n):
            prices[i]-=min_nums[i]
        return max(prices)