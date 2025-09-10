class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp=[-1]*(amount+1)
        # dp[0]=0
        # n=len(coins)
        # if amount==0:
        #     return 0
        # if amount<min(coins):
        #     return -1
        # coins_sort=sorted(coins)
        # for i in  range(1,amount+1):
        #     for j in range(n):
        #         nums_k=i/coins_sort[j]
        #         for z in range(1,nums_k+1):
        #             sum=i-z*coins_sort[j]
        #             if dp[sum]!=-1:
        #                 if dp[i]==-1 or dp[sum]+z<dp[i]:
        #                     dp[i]=z+dp[sum]
        # return dp[amount]
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        # coins.sort()
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin and dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        if dp[amount] == float('inf'):
            dp[amount] = -1
        return dp[amount]