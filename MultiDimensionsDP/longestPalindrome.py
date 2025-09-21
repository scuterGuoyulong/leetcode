class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        max_pal = s[0]
        for i in range(n):
            sub_pal = expand(s,i,i)
            if len(sub_pal) > len(max_pal):
                max_pal = sub_pal
            if i+1<=n-1:
                sub_pal = expand(s,i,i+1)
                if len(sub_pal) > len(max_pal):
                    max_pal = sub_pal
        return max_pal


def expand(s,i,j):
    n=len(s)
    if i==j:
        while i>=0 and j<n and s[i]==s[j] :
            i-=1
            j+=1
        ans=s[i+1:j]
    else:
        if s[i]!=s[j]:
            ans=""
        else:
            while i>=0 and j<n and s[i]==s[j] :
                i -= 1
                j += 1
            ans = s[i + 1:j]
    return ans