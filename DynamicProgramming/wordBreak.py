class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n=len(s)
        dp=[False]*(n+1)
        dp[0] = True
        for i in range(n):
            for word in wordDict:
                word_len = len(word)
                if s[i-word_len:i]==word and dp[i-word_len] and i>=word_len:
                    dp[i]=True
                    break
        return dp[n]

